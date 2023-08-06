# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:25:34 2018

@author: yoelr
"""
from ._exceptions import DimensionError, biosteamError
from ._utils import DisplayUnits
from ._species import Species
from ._stream import Stream, mol_flow_dim, mass_flow_dim, vol_flow_dim
import pandas as pd
from . import _Q


__all__ = ('HeatUtility',)

# Costs from Table 17.1 in Warren D.  Seider et al.-Product and Process Design Principles_ Synthesis, Analysis and Evaluation-Wiley (2016)
# ^This table was made using data from Busche, 1995
# Entry temperature conditions of coolants taken from Table 12.1 in Warren, 2016

# %% Default Heat Transfer species

_Water = Species('Water')

# %% Data for cooling utilities 

_columns = ('Species', 'Molar fraction', 'Temperature (K)', 'Pressure (Pa)',
            'Phase', 'Latent heat (kJ/kmol)', 'Temperature limit (K)',
            'Price (USD/kJ)', 'Price (USD/kmol)', 'Heat transfer efficiency')

_cooling_index = ('Cooling water',
                  'Chilled water',
                  'Chilled Brine')

_cooling_water = (_Water,          # species [Species]
                  (1,),            # flow: [tuple]
                  305.372,         # T (K)
                  101325,          # P (Pa)
                  'liq',           # phase: {'g', 'l'}
                  None,            # latent heat (kJ/kmol)
                  324.817,         # T limit (K)
                  0,               # price (USD/kJ)
                  4.8785e-4,       # price (USD/kmol)
                  1)               # heat transfer efficiency

_chilled_water = (_Water,
                  (1,),
                  280.372,
                  101325,
                  'liq',
                  None,
                  300.372,
                  -5e-6,
                  0,
                  1)

_chilled_brine = (_Water,
                  (1,),
                  255.372,
                  101325,
                  'liq',
                  None,
                  275.372,
                  -8.145e-6,
                  0,
                  1)


# %% Data for heating utilities

_heating_index = ('Low pressure steam',
                  'Medium pressure steam',
                  'High pressure steam')

_low_pressure_steam = (_Water,
                       (1,),
                       411.494,
                       344738.0,
                       'gas',
                       3.89e+04,
                       None,
                       0,
                       0.2378,
                       0.95)

_medium_pressure_steam = (_Water,
                          (1,),
                          454.484,
                          1034214.0,
                          'gas',
                          3.63e+04,
                          None,
                          0,
                          0.2756,
                          0.90)

_high_pressure_steam = (_Water,
                        (1,),
                        508.858,
                        3102642.0,
                        'gas',
                        3.21e+04,
                        None,
                        0,
                        0.3171,
                        0.85)


# %% Utility classes


class HeatUtility:
    """Create an HeatUtility object that can choose a utility stream and calculate utility requirements. It can calculate required flow rate, temperature, or phase change of utility. Calculations assume counter current flow rate.
    
    **Parameters**
    
        **efficiency:** [float] Fraction of heat transfered after accounting for heat loss.
    
    **Class Attributes**

        **cooling_agents:** [DataFrame] All cooling utilities available
        
        **heating_agents:** [DataFrame] All heating utilities available
    
    **Examples**
    
        Create a heat utility:
            
        .. code-block:: python
        
           >>> hu = HeatUtility()
           >>> hu
           HeatUtility: None
            duty: 0
            flow: 0
            cost: 0
        
        Calculate utility requirement by calling it with a duty (kJ/hr) and temperature (K):
            
        .. code-block:: python
        
           >>> hu(1000, 300, 350)
           >>> hu
           HeatUtility: Low pressure steam
            duty: 1.11e+03 kJ/hr
            flow: 0.0284 kmol/hr,
            cost: 0.00674 USD/hr
       
        All results are accessible:
            
        .. code-block:: python
        
           >>> hu.ID, hu.duty, hu.flow, hu.cost
           ('Low pressure steam',
            1111.111111111111,
            0.028351477551759364,
            0.006741981361808377)
           
    """
    __slots__ = ('_fresh', '_used', 'ID', 'duty',
                 'flow', 'cost', 'efficiency',
                 '_args')
    dT = 5  #: [float] Pinch temperature difference
    
    #: Units of measure for results dictionary
    _units = dict(duty='kJ/hr', flow='kmol/hr', cost='USD/hr')
    
    #: [DisplayUnits] Units of measure for IPython display
    display_units = DisplayUnits(**_units)

    # All cooling utilities available
    cooling_agents = pd.DataFrame([_cooling_water,
                                   _chilled_water,
                                   _chilled_brine],
                                  columns=_columns,
                                  index=_cooling_index).transpose()

    # All heating utilities available
    heating_agents = pd.DataFrame([_low_pressure_steam,
                                   _medium_pressure_steam,
                                   _high_pressure_steam],
                                  columns=_columns,
                                  index=_heating_index).transpose()

    def __init__(self, efficiency=None):
        self.ID = ''
        self.cost = self.flow = self.duty = 0
        self.efficiency = efficiency
        
        #: tuple[bool, float] Cached arguments:
        #:     * [0]: [bool] True if duty is negative 
        #:     * [1]: [float] Temperature of operation
        self._args = None

    def _init_streams(self, flow, species, T, P, phase):
        """Initialize utility streams."""
        self._fresh = Stream(None, flow, species, T=T, P=P, phase=phase)
        self._used = Stream.proxy(None, self._fresh)

    def __call__(self, duty, T_in, T_out=None):
        """Calculate utility requirements given the essential parameters.
        
        **Parameters**
        
            **duty:** [float] Unit duty requirement (kJ/hr)
            
            **T_in:** [float] Entering process stream temperature (K)
            
            **T_out:** [float] Exit process stream temperature (K)
        
        """
        # Set pinch and operating temperature
        if T_out is None:
            T_pinch = T_op = T_in
        else:
            T_pinch, T_op = self._get_pinch(duty, T_in, T_out)
        
        if duty == 0:
            self.ID = ''
            self.flow = self.duty = self.cost = 0
            self._args = None
            return
        
        negduty = duty < 0
        args = (negduty, T_op)
        if self._args != args:
            self._args = args
            # Select heat transfer agent
            if negduty:
                (latent_heat, price_duty,
                 price_mol, T_limit,
                 efficiency) = self._select_cooling_agent(T_op)
            else:
                (latent_heat, price_duty,
                price_mol, T_limit,
                efficiency) = self._select_heating_agent(T_op)
        else:
            if negduty:
                (*_, latent_heat, T_limit,
                 price_duty, price_mol, efficiency) = self.cooling_agents[self.ID]
            else:
                (*_, latent_heat, T_limit,
                 price_duty, price_mol, efficiency) = self.heating_agents[self.ID]
        
        # Calculate utility flow rate requirement
        efficiency = self.efficiency if self.efficiency else efficiency
        duty = duty/efficiency
        if latent_heat:
            self._update_flow_wt_phase_change(duty, latent_heat)
        else:
            self._update_flow_wt_pinch_T(duty, T_pinch, T_limit, negduty)
        
        # Update and return results
        self.flow = mol = self._fresh.molnet
        self.duty = duty
        self.cost = price_duty*duty + price_mol*mol

    @staticmethod
    def _get_pinch(duty, T_in, T_out):
        """Return pinch temperature and operating temperature."""
        if duty < 0:
            return (T_in, T_out) if T_in > T_out else (T_out, T_in)
        else:
            return (T_in, T_out) if T_in < T_out else (T_out, T_in)
    
    # Selection of a heat transfer agent
    def _select_cooling_agent(self, T_pinch):
        """Select a cooling agent that works at the pinch temperature and return relevant information.
        
        **Parameters**

             **T_pinch:**  [float] Pinch temperature of process stream (K)
        
        **Returns**
        
            **latent_heat:** [float] (kJ/kmol)
            
            **price_duty:** [float] (USD/kJ)
            
            **price_mass:** [float] (USD/kg)
            
            **T_limit:** [float] Maximum or minimum temperature of agent (K)
            
            **efficiency:** [float] Heat transfer efficiency
        
        """
        dt = 2*self.dT
        T_max = T_pinch - dt
        cooling_agents = self.cooling_agents
        for ID in cooling_agents:
            (species, flow, T, P, phase,
             latent_heat, T_limit, price_duty,
             price_mol, efficiency) = cooling_agents[ID]
            if T_max > T:
                if self.ID != ID:
                    self._init_streams(flow, species, T, P, phase[0])
                    self.ID = ID
                return (latent_heat, price_duty, price_mol, T_limit, efficiency)
        raise biosteamError(f'no cooling agent that can cool under {T_pinch} K')
            
    def _select_heating_agent(self, T_pinch):
        """Select a heating agent that works at the pinch temperature and return relevant information.
        
        **Parameters**

             **T_pinch:**  [float] Pinch temperature of process stream (K)
        
        **Returns**
        
            **latent_heat:** [float] (kJ/kmol)
            
            **price_duty:** [float] (USD/kJ)
            
            **price_mass:** [float] (USD/kg)
            
            **T_limit:** [float] Maximum or minimum temperature of agent (K)
            
            **efficiency:** [float] Heat transfer efficiency
        
        """
        dt = 2*self.dT
        T_min = T_pinch + dt
        heating_agents = self.heating_agents
        for ID in heating_agents:
            (species, flow, T, P, phase,
             latent_heat, T_limit, price_duty,
             price_mol, efficiency) =  heating_agents[ID]
            if T_min < T:
                if self.ID != ID:
                    self._init_streams(flow, species, T, P, phase[0])
                    self.ID = ID
                return (latent_heat, price_duty, price_mol, T_limit, efficiency)
        raise biosteamError(f'no heating agent that can heat over {T_pinch} K')

    # Main Calculations
    def _update_flow_wt_pinch_T(self, duty, T_pinch, T_limit, negduty):
        """Set utility Temperature at the pinch, calculate and set minimum net flowrate of the utility to satisfy duty and update."""
        self._used.T = self._T_exit(T_pinch, self.dT, T_limit, negduty)
        self._update_utility_flow(self._fresh, self._used, duty)

    def _update_flow_wt_phase_change(self, duty, latent_heat):
        """Change phase of utility, calculate and set minimum net flowrate of the utility to satisfy duty and update."""
        f = self._fresh
        u = self._used
        u._phase = 'g' if f._phase=='l' else 'l'
        u._mol[:] = duty/latent_heat

    # Subcalculations
    @staticmethod
    def _update_utility_flow(fresh, utility, duty):
        """Changes flow rate of utility such that it can meet the duty requirement"""
        utility._mol *= duty/(fresh.H - utility.H)

    @staticmethod
    def _T_exit(T_pinch, dT, T_limit, negduty):
        """Return exit temperature of the utility in a counter current heat exchanger

        **Parameters**

             **T_pinch:** [float] Pinch temperature of process stream (K)

             **dT:** [float] Pinch temperature difference (K)

             **negduty:** [bool] True if exit temperature should be lower (process stream is gaining energy)

        """
        if negduty:
            T_exit = T_pinch - dT
            if T_limit and T_limit < T_exit: T_exit = T_limit
        else:
            T_exit = T_pinch + dT
            if T_limit and T_limit > T_exit: T_exit = T_limit
        return T_exit

    def _info_data(self, duty, flow, cost):
        # Get units of measure
        su = self.display_units
        units = self._units
        duty_units = duty or su.duty
        flow_units = flow or su.flow
        cost_units = cost or su.cost
        
        # Select flow dimensionality
        flow_dim = _Q(0, flow_units).dimensionality
        if flow_dim == mol_flow_dim:
            flowattr = 'molnet'
        elif flow_dim == mass_flow_dim:
            flowattr = 'massnet'
        elif flow_dim == vol_flow_dim:
            flowattr = 'volnet'
        else:
            raise DimensionError(f"dimensions for flow units must be in molar, mass or volumetric flow rates, not '{flow_dim}'")
        
        # Change units and return info string
        try:
            u_in = self._fresh
            flownet = getattr(u_in, flowattr)
            flowunits = u_in.units[flowattr]
            flow = _Q(flownet, flowunits).to(flow_units).magnitude
        except:
            flow = _Q(self.flow, 'kmol/hr').to(flow_units).magnitude
        
        duty = _Q(self.duty, units['duty']).to(duty_units).magnitude
        cost = _Q(self.cost, units['cost']).to(cost_units).magnitude
        return duty, flow, cost, duty_units, flow_units, cost_units
        
    def __repr__(self):
        if self.ID:
            duty, flow, cost, duty_units, flow_units, cost_units = self._info_data(None, None, None)
            return f'<{self.ID}: {self.duty:.3g} {duty_units}, {self.flow:.3g} {flow_units}, {self.cost:.3g} {cost_units}>'
        else:
            return f'<{type(self).__name__}: None>'
        
    # Representation
    def _info(self, duty, flow, cost):
        """Return string related to specifications"""
        if not self.ID:
            return (f'{type(self).__name__}: None\n'
                    +f' duty: 0\n'
                    +f' flow: 0\n'
                    +f' cost: 0')
        else:
            (duty, flow, cost, duty_units,
             flow_units, cost_units) = self._info_data(duty, flow, cost)
            return (f'{type(self).__name__}: {self.ID}\n'
                    +f' duty:{duty: .3g} {duty_units}\n'
                    +f' flow:{flow: .3g} {flow_units}\n'
                    +f' cost:{cost: .3g} {cost_units}')
            

    def show(self, duty=None, flow=None, cost=None):
        """Print all specifications"""
        print(self._info(duty, flow, cost))
    _ipython_display_ = show


del _Water, _columns, _cooling_index, _cooling_water, _chilled_water, \
    _chilled_brine, _heating_index, _low_pressure_steam, \
    _medium_pressure_steam, _high_pressure_steam