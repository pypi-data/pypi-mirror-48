# -*- coding: utf-8 -*-
"""
pmutt.empirical.nasa

Operations related to Nasa polynomials
"""

import inspect
from warnings import warn
import numpy as np
from scipy.stats import variation
from pmutt import _is_iterable, _pass_expected_arguments
from pmutt import constants as c
from pmutt.io.json import json_to_pmutt, remove_class
from pmutt.empirical import EmpiricalBase
from pmutt.mixture import _get_mix_quantity


class Nasa(EmpiricalBase):
    """Stores the information for an individual nasa specie
    Inherits from :class:`~pmutt.empirical.EmpiricalBase`

    The thermodynamic properties are calculated using the following form:

    :math:`\\frac {Cp} {R} = a_{1} + a_{2} T + a_{3} T^{2} + a_{4} T^{3}
    + a_{5} T^{4}`

    :math:`\\frac {H} {RT} = a_{1} + a_{2} \\frac {T} {2} + a_{3}
    \\frac {T^{2}} {3} + a_{4} \\frac {T^{3}} {4} + a_{5}
    \\frac {T^{4}} {5} + a_{6} \\frac {1} {T}`

    :math:`\\frac {S} {R} = a_{1} \\ln {T} + a_{2} T + a_{3}
    \\frac {T^{2}} {2} + a_{4} \\frac {T^{3}} {3} + a_{5}
    \\frac {T^{4}} {4} + a_{7}`

    Attributes
    ----------
        T_low : float
            Lower temperature bound (in K)
        T_mid : float
            Middle temperature bound (in K)
        T_high : float
            High temperature bound (in K)
        a_low : (7,) `numpy.ndarray`_
            NASA polynomial to use between T_low and T_mid
        a_high : (7,) `numpy.ndarray`_
            NASA polynomial to use between T_mid and T_high
        cat_site : Site object, optional
            Catalyst site for adsorption. Default is None
        n_sites : int, optional
            Number of catalyst sites occupied by species. If cat_site is not
            assigned, then n_sites is None. If cat_site is specified, the
            default is 1

    .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    """
    def __init__(self, name, T_low, T_mid, T_high, a_low, a_high,
                 cat_site=None, n_sites=1, **kwargs):
        super().__init__(name=name, **kwargs)
        self.T_low = T_low
        self.T_mid = T_mid
        self.T_high = T_high
        self.a_low = np.array(a_low)
        self.a_high = np.array(a_high)
        if inspect.isclass(cat_site):
            self.cat_site = _pass_expected_arguments(cat_site, **kwargs)
        else:
            self.cat_site = cat_site
        if self.cat_site is None:
            n_sites = None
        self.n_sites = n_sites

    def get_a(self, T):
        """Returns the correct polynomial range based on T_low, T_mid and
        T_high

        Parameters
        ----------
            T : float
                Temperature in K
        Returns
        -------
            a : (7,) `numpy.ndarray`_
                NASA polynomial coefficients

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        if type(self.T_mid) is list:
            self.T_mid = self.T_mid[0]
        if T < self.T_mid:
            if T < self.T_low:
                warn('Temperature below T_low for {}'.format(self.name),
                     RuntimeWarning)
            return self.a_low
        else:
            if T > self.T_high:
                warn('Temperature above T_high for {}'.format(self.name),
                     RuntimeWarning)
            return self.a_high

    def get_CpoR(self, T, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the dimensionless heat capacity

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            CpoR : float or (N,) `numpy.ndarray`_
                Dimensionless heat capacity

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        if _is_iterable(T):
            CpoR = np.zeros(len(T))
            for i, T_i in enumerate(T):
                a = self.get_a(T_i)
                CpoR[i] = get_nasa_CpoR(a=a, T=T_i) \
                    + np.sum(_get_mix_quantity(self.misc_models,
                                               method_name='get_CpoR',
                                               raise_error=raise_error,
                                               raise_warning=raise_warning,
                                               default_value=0.,
                                               T=T_i, **kwargs))
        else:
            a = self.get_a(T=T)
            CpoR = get_nasa_CpoR(a=a, T=T) \
                + np.sum(_get_mix_quantity(self.misc_models, 
                                           method_name='get_CpoR',
                                           raise_error=raise_error,
                                           raise_warning=raise_warning,
                                           default_value=0.,
                                           T=T, **kwargs))
        return CpoR

    def get_Cp(self, T, units, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the heat capacity

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            units : str
                Units as string. See :func:`~pmutt.constants.R` for accepted
                units.
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            Cp : float or (N,) `numpy.ndarray`_
                Heat capacity

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        return self.get_CpoR(T=T)*c.R(units)

    def get_HoRT(self, T, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the dimensionless enthalpy

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            HoRT : float or (N,) `numpy.ndarray`_
                Dimensionless enthalpy

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        if _is_iterable(T):
            HoRT = np.zeros_like(T)
            for i, T_i in enumerate(T):
                a = self.get_a(T=T_i)
                HoRT[i] = get_nasa_HoRT(a=a, T=T_i) \
                    + np.sum(_get_mix_quantity(misc_models=self.misc_models,
                                               method_name='get_HoRT',
                                               raise_error=raise_error,
                                               raise_warning=raise_warning,
                                               default_value=0.,
                                               T=T_i, **kwargs))
        else:
            a = self.get_a(T=T)
            HoRT = get_nasa_HoRT(a=a, T=T) \
                + np.sum(_get_mix_quantity(misc_models=self.misc_models,
                                           method_name='get_HoRT',
                                           raise_error=raise_error,
                                           raise_warning=raise_warning,
                                           default_value=0.,
                                           T=T, **kwargs))
        return HoRT

    def get_H(self, T, units, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the enthalpy

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            units : str
                Units as string. See :func:`~pmutt.constants.R` for accepted
                units but omit the '/K' (e.g. J/mol).
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            H : float or (N,) `numpy.ndarray`_
                Enthalpy

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        return self.get_HoRT(T=T, raise_error=raise_error,
                             raise_warning=raise_warning, **kwargs) \
               *T*c.R('{}/K'.format(units))

    def get_SoR(self, T, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the dimensionless entropy

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            SoR : float or (N,) `numpy.ndarray`_
                Dimensionless entropy

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        if _is_iterable(T):
            SoR = np.zeros_like(T)
            for i, T_i in enumerate(T):
                a = self.get_a(T=T_i)
                SoR[i] = get_nasa_SoR(a=a, T=T_i) \
                    + np.sum(_get_mix_quantity(misc_models=self.misc_models,
                                               method_name='get_SoR',
                                               raise_error=raise_error,
                                               raise_warning=raise_warning,
                                               default_value=0.,
                                               T=T_i, **kwargs))
        else:
            a = self.get_a(T=T)
            SoR = get_nasa_SoR(a=a, T=T) \
                + np.sum(_get_mix_quantity(misc_models=self.misc_models,
                                           method_name='get_SoR',
                                           raise_error=raise_error,
                                           raise_warning=raise_warning,
                                           default_value=0.,
                                           T=T, **kwargs))
        return SoR

    def get_S(self, T, units, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the entropy

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            units : str
                Units as string. See :func:`~pmutt.constants.R` for accepted
                units.
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            S : float or (N,) `numpy.ndarray`_
                Entropy

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        return self.get_SoR(T=T, raise_error=raise_error,
                            raise_warning=raise_warning, **kwargs)*c.R(units)

    def get_GoRT(self, T, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the dimensionless Gibbs free energy

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            GoRT : float or (N,) `numpy.ndarray`_
                Dimensionless Gibbs free energy

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        GoRT = self.get_HoRT(T, raise_error=raise_error,
                             raise_warning=raise_warning, **kwargs) \
               - self.get_SoR(T, raise_error=raise_error,
                              raise_warning=raise_warning, **kwargs)
        return GoRT

    def get_G(self, T, units, raise_error=True, raise_warning=True, **kwargs):
        """Calculate the Gibbs energy

        Parameters
        ----------
            T : float or (N,) `numpy.ndarray`_
                Temperature(s) in K
            units : str
                Units as string. See :func:`~pmutt.constants.R` for accepted
                units but omit the '/K' (e.g. J/mol).
            raise_error : bool, optional
                If True, raises an error if any of the modes do not have the
                quantity of interest. Default is True
            raise_warning : bool, optional
                Only relevant if raise_error is False. Raises a warning if any
                of the modes do not have the quantity of interest. Default is
                True
            kwargs : key-word arguments
                Arguments to calculate mixture model properties, if any
        Returns
        -------
            G : float or (N,) `numpy.ndarray`_
                Gibbs energy

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        return self.get_GoRT(T=T, raise_error=raise_error,
                             raise_warning=raise_warning, **kwargs) \
            * T*c.R('{}/K'.format(units))

    @classmethod
    def from_data(cls, name, T, CpoR, T_ref, HoRT_ref, SoR_ref, elements=None,
                  T_mid=None, **kwargs):
        """Calculates the NASA polynomials using thermodynamic data

        Parameters
        ----------
            name : str
                Name of the species
            T : (N,) `numpy.ndarray`_
                Temperatures in K used for fitting CpoR.
            CpoR : (N,) `numpy.ndarray`_
                Dimensionless heat capacity corresponding to T.
            T_ref : float
                Reference temperature in K used fitting empirical coefficients.
            HoRT_ref : float
                Dimensionless reference enthalpy that corresponds to T_ref.
            SoR_ref : float
                Dimensionless entropy that corresponds to T_ref.
            elements : dict
                Composition of the species.
                Keys of dictionary are elements, values are stoichiometric
                values in a formula unit.
                e.g. CH3OH can be represented as:
                {'C': 1, 'H': 4, 'O': 1,}.
            T_mid : float or iterable of float, optional
                Guess for T_mid. If float, only uses that value for T_mid. If
                list, finds the best fit for each element in the list. If None,
                a range of T_mid values are screened between the 6th lowest
                and 6th highest value of T.
        Returns
        -------
            Nasa : Nasa object
                Nasa object with polynomial terms fitted to data.

        .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        T_low = min(T)
        T_high = max(T)

        # Find midpoint temperature, and a[0] through a[4] parameters
        a_low, a_high, T_mid_out = _fit_CpoR(T=T, CpoR=CpoR, T_mid=T_mid)
        # Fit a[5] parameter using reference enthalpy
        a_low[5], a_high[5] = _fit_HoRT(T_ref=T_ref, HoRT_ref=HoRT_ref,
                                        a_low=a_low, a_high=a_high,
                                        T_mid=T_mid_out)
        # Fit a[6] parameter using reference entropy
        a_low[6], a_high[6] = _fit_SoR(T_ref=T_ref, SoR_ref=SoR_ref,
                                       a_low=a_low, a_high=a_high,
                                       T_mid=T_mid_out)
        return cls(name=name, T_low=T_low, T_high=T_high, T_mid=T_mid_out,
                   a_low=a_low, a_high=a_high, elements=elements, **kwargs)

    @classmethod
    def from_statmech(cls, name, statmech_model, T_low, T_high, T_mid=None,
                      references=None, elements=None, **kwargs):
        """Calculates the NASA polynomials using statistical mechanic models

        Parameters
        ----------
            name : str
                Name of the species
            statmech_model : `pmutt.statmech.StatMech` object or class
                Statistical Mechanics model to generate data
            T_low : float
                Lower limit temerature in K
            T_high : float
                Higher limit temperature in K
            T_mid : float or iterable of float, optional
                Guess for T_mid. If float, only uses that value for T_mid. If
                list, finds the best fit for each element in the list. If None,
                a range of T_mid values are screened between the 6th lowest
                and 6th highest value of T.
            references : `pmutt.empirical.references.References` object
                Reference to adjust enthalpy
            elements : dict
                Composition of the species.
                Keys of dictionary are elements, values are stoichiometric
                values in a formula unit.
                e.g. CH3OH can be represented as:
                {'C': 1, 'H': 4, 'O': 1,}.
            kwargs : keyword arguments
                Used to initalize ``statmech_model`` or ``EmpiricalBase``
                attributes to be stored.
        Returns
        -------
            Nasa : Nasa object
                Nasa object with polynomial terms fitted to data.
        """
        # Initialize the StatMech object
        if inspect.isclass(statmech_model):
            statmech_model = statmech_model(name=name, references=references,
                                            elements=elements, **kwargs)

        # Generate heat capacity data
        T = np.linspace(T_low, T_high)
        if T_mid is not None:
            # Check to see if specified T_mid's are in T and, if not,
            # insert them into T.
            # If a single value for T_mid is chosen, convert to a tuple
            if not _is_iterable(T_mid):
                T_mid = (T_mid,)
            for x in range(0, len(T_mid)):
                if np.where(T == T_mid[x])[0].size == 0:
                    # Insert T_mid's into T and save position
                    Ts_index = np.where(T > T_mid[x])[0][0]
                    T = np.insert(T, Ts_index, T_mid[x])
        CpoR = np.array(
            [statmech_model.get_CpoR(T=T_i, use_references=True) for T_i in T])
        # Generate enthalpy and entropy data
        T_ref = c.T0('K')
        HoRT_ref = statmech_model.get_HoRT(T=T_ref, use_references=True)
        SoR_ref = statmech_model.get_SoR(T=T_ref, use_references=True)

        return cls.from_data(name=name, T=T, CpoR=CpoR, T_ref=T_ref,
                             HoRT_ref=HoRT_ref, SoR_ref=SoR_ref, T_mid=T_mid,
                             statmech_model=statmech_model, elements=elements,
                             references=references, **kwargs)

    def to_dict(self):
        """Represents object as dictionary with JSON-accepted datatypes

        Returns
        -------
            obj_dict : dict
        """
        obj_dict = super().to_dict()
        obj_dict['class'] = str(self.__class__)
        obj_dict['type'] = 'nasa'
        obj_dict['a_low'] = list(self.a_low)
        obj_dict['a_high'] = list(self.a_high)
        obj_dict['T_low'] = self.T_low
        obj_dict['T_mid'] = self.T_mid
        obj_dict['T_high'] = self.T_high
        try:
            obj_dict['cat_site'] = self.cat_site.to_dict()
        except AttributeError:
            obj_dict['cat_site'] = None
        obj_dict['n_sites'] = self.n_sites
        return obj_dict

    @classmethod
    def from_dict(cls, json_obj):
        """Recreate an object from the JSON representation.

        Parameters
        ----------
            json_obj : dict
                JSON representation
        Returns
        -------
            Nasa : Nasa object
        """
        json_obj = remove_class(json_obj)
        # Reconstruct statmech model
        json_obj['statmech_model'] = json_to_pmutt(json_obj['statmech_model'])
        json_obj['cat_site'] = json_to_pmutt(json_obj['cat_site'])
        json_obj['misc_models'] = json_to_pmutt(json_obj['misc_models'])
        return cls(**json_obj)


def _fit_CpoR(T, CpoR, T_mid=None):
    """Fit a[0]-a[4] coefficients in a_low and a_high attributes given the
    dimensionless heat capacity data

    Parameters
    ----------
        T : (N,) `numpy.ndarray`_
            Temperatures in K
        CpoR : (N,) `numpy.ndarray`_
            Dimensionless heat capacity
        T_mid : float or iterable of float, optional
            Guess for T_mid. If float, only uses that value for T_mid. If
            list, finds the best fit for each element in the list. If None,
            a range of T_mid values are screened between the lowest value
            and highest value of T.
    Returns
    -------
        a_low : (7,) `numpy.ndarray`_
            Lower coefficients of NASA polynomial
        a_high : (7,) `numpy.ndarray`_
            Higher coefficients of NASA polynomial
        T_mid : float
            Temperature in K used to split the CpoR data


    .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    """
    # If the Cp/R does not vary with temperature (occurs when no
    # vibrational frequencies are listed), return default values
    if (np.isclose(np.mean(CpoR), 0.) and np.isnan(variation(CpoR))) \
       or np.isclose(variation(CpoR), 0.) \
       or any([np.isnan(x) for x in CpoR]):
        T_mid = T[int(len(T)/2)]
        a_low = np.zeros(7)
        a_high = np.zeros(7)
        return a_low, a_high, T_mid

    # If T_mid not specified, generate range between 6th smallest data point
    # and 6th largest data point
    if T_mid is None:
        T_mid = T[5:-5]

    # If a single value for T_mid is chosen, convert to a tuple
    if not _is_iterable(T_mid):
        T_mid = (T_mid,)

    # Initialize parameters for T_mid optimization
    mse_list = []
    prev_mse = np.inf
    all_a_low = []
    all_a_high = []
    for T_m in T_mid:
        # Generate temperature data
        (mse, a_low, a_high) = _get_CpoR_MSE(T=T, CpoR=CpoR, T_mid=T_m)
        mse_list.append(mse)
        all_a_low.append(a_low)
        all_a_high.append(a_high)
        # Check if the optimum T_mid has been found by determining if the
        # fit MSE value for the current T_mid is higher than the previous
        # indicating that subsequent guesses will not improve the fit
        if mse > prev_mse:
            break
        prev_mse = mse

    # Select the optimum T_mid based on the highest fit R2 value
    min_mse = min(mse_list)
    min_i = np.where(min_mse == mse_list)[0][0]

    T_mid_out = T_mid[min_i]
    a_low_rev = all_a_low[min_i]
    a_high_rev = all_a_high[min_i]

    # Reverse array and append two zeros to end
    empty_arr = np.zeros(2)
    a_low_out = np.concatenate((a_low_rev[::-1], empty_arr))
    a_high_out = np.concatenate((a_high_rev[::-1], empty_arr))
    return a_low_out, a_high_out, T_mid_out


def _get_CpoR_MSE(T, CpoR, T_mid):
    """Calculates the mean squared error of polynomial fit.

    Parameters
    ----------
        T : (N,) `numpy.ndarray`_
            Temperatures (K) to fit the polynomial
        CpoR : (N,) `numpy.ndarray`_
            Dimensionless heat capacities that correspond to T array
        i_mid : int
            Index that splits T and CpoR arrays into a lower
            and higher range
    Returns
    -------
        mse : float
            Mean squared error resulting from NASA polynomial fit to T and CpoR
        p_low : (5,) `numpy.ndarray`_
            Polynomial corresponding to lower range of data
        p_high : (5,) `numpy.ndarray`_
            Polynomial corresponding to high range of data

    .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    """
    low_condition = (T <= T_mid)
    high_condition = (T > T_mid)
    T_low = np.extract(condition=low_condition, arr=T)
    T_high = np.extract(condition=high_condition, arr=T)
    CpoR_low = np.extract(condition=low_condition, arr=CpoR)
    CpoR_high = np.extract(condition=high_condition, arr=CpoR)

    if len(T_low) < 5:
        warn('Small set of CpoR data between T_low and T_mid. '
             'Fit may not be desirable.', RuntimeWarning)
    if len(T_high) < 5:
        warn('Small set of CpoR data between T_mid and T_high. '
             'Fit may not be desirable.', RuntimeWarning)

    # Fit the polynomials
    p_low = np.polyfit(x=T_low, y=CpoR_low, deg=4)
    p_high = np.polyfit(x=T_high, y=CpoR_high, deg=4)

    # Calculate RMSE
    CpoR_low_fit = np.polyval(p_low, T_low)
    CpoR_high_fit = np.polyval(p_high, T_high)
    CpoR_fit = np.concatenate((CpoR_low_fit, CpoR_high_fit))
    mse = np.mean([(x-y)**2 for x, y in zip(CpoR, CpoR_fit)])
    return (mse, p_low, p_high)


def _fit_HoRT(T_ref, HoRT_ref, a_low, a_high, T_mid):
    """Fit a[5] coefficient in a_low and a_high attributes given the
    dimensionless enthalpy

    Parameters
    ----------
        T_ref : float
            Reference temperature in K
        HoRT_ref : float
            Reference dimensionless enthalpy
        T_mid : float
            Temperature to fit the offset
    Returns
    -------
        a6_low_out : float
            Lower a6 value for NASA polynomial
        a6_high_out : float
            Higher a6 value for NASA polynomial
    """
    a6_low_out = (HoRT_ref - get_nasa_HoRT(a=a_low, T=T_ref))*T_ref
    a6_high = (HoRT_ref - get_nasa_HoRT(a=a_high, T=T_ref))*T_ref

    # Correcting for offset
    H_low_last_T = get_nasa_HoRT(a=a_low, T=T_mid) + a6_low_out/T_mid
    H_high_first_T = get_nasa_HoRT(a=a_high, T=T_mid) + a6_high/T_mid
    H_offset = H_low_last_T - H_high_first_T
    a6_high_out = T_mid * (a6_high/T_mid + H_offset)

    return a6_low_out, a6_high_out


def _fit_SoR(T_ref, SoR_ref, a_low, a_high, T_mid):
    """Fit a[6] coefficient in a_low and a_high attributes given the
    dimensionless entropy

    Parameters
    ----------
        T_ref : float
            Reference temperature in K
        SoR_ref : float
            Reference dimensionless entropy
        T_mid : float
            Temperature to fit the offset
    Returns
    -------
        a7_low_out : float
            Lower a7 value for NASA polynomial
        a7_high_out : float
            Higher a7 value for NASA polynomial
    """
    a7_low_out = SoR_ref - get_nasa_SoR(a=a_low, T=T_ref)
    a7_high = SoR_ref - get_nasa_SoR(a=a_high, T=T_ref)

    # Correcting for offset
    S_low_last_T = get_nasa_SoR(a=a_low, T=T_mid) + a7_low_out
    S_high_first_T = get_nasa_SoR(a=a_high, T=T_mid) + a7_high
    S_offset = S_low_last_T - S_high_first_T
    a7_high_out = a7_high + S_offset

    return a7_low_out, a7_high_out


def get_nasa_CpoR(a, T):
    """Calculates the dimensionless heat capacity using NASA polynomial form

    Parameters
    ----------
        a : (7,) `numpy.ndarray`_
            Coefficients of NASA polynomial
        T : float
            Temperature in K
    Returns
    -------
        CpoR: float
            Dimensionless heat capacity

    .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    """
    T_arr = np.array([1., T, T**2, T**3, T**4, 0., 0.])
    return np.dot(a, T_arr)


def get_nasa_HoRT(a, T):
    """Calculates the dimensionless enthalpy using NASA polynomial form

    Parameters
    ----------
        a : (7,) `numpy.ndarray`_
            Coefficients of NASA polynomial
        T : float
            Temperature in K
    Returns
    -------
        HoRT : float
            Dimensionless enthalpy

    .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    """
    T_arr = np.array([1., T/2., (T**2)/3., (T**3)/4., (T**4)/5., 1./T, 0.])
    return np.dot(a, T_arr)


def get_nasa_SoR(a, T):
    """Calculates the dimensionless entropy using NASA polynomial form

    Parameters
    ----------
        a : (7,) `numpy.ndarray`_
            Coefficients of NASA polynomial
        T : float
            Temperature in K
    Returns
    -------
        SoR : float
            Dimensionless entropy

    .. _`numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    """
    T_arr = np.array([np.log(T), T, (T**2)/2., (T**3)/3., (T**4)/4., 0., 1.])
    return np.dot(a, T_arr)
