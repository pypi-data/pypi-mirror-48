# -*- coding: utf-8 -*-

import datetime

from openfisca_core import periods

from openfisca_france.scenarios import init_single_entity

from openfisca_france.reforms.plf2016 import plf2016, plf2016_counterfactual, plf2016_counterfactual_2014
from ..cache import tax_benefit_system


def test_plf2016(year = 2015):
    run(plf2016, 2015)
    run(plf2016_counterfactual, 2015)
    run(plf2016_counterfactual_2014, 2015)


def run(reform_class, year):
    max_sal = 18000
    count = 2
    people = 1
    reform = reform_class(tax_benefit_system)
    scenario = init_single_entity(reform.new_scenario(),
        axes = [[
            dict(
                count = count,
                max = max_sal,
                min = 0,
                name = 'salaire_imposable',
                ),
            ]],
        period = periods.period(year),
        parent1 = dict(date_naissance = datetime.date(year - 40, 1, 1)),
        parent2 = dict(date_naissance = datetime.date(year - 40, 1, 1)) if people >= 2 else None,
        enfants = [
            dict(date_naissance = datetime.date(year - 9, 1, 1)) if people >= 3 else None,
            dict(date_naissance = datetime.date(year - 9, 1, 1)) if people >= 4 else None,
            ] if people >= 3 else None,
        )

    reference_simulation = scenario.new_simulation(use_baseline = True)
    reform_simulation = scenario.new_simulation()
#    error_margin = 1

    impo = reference_simulation.calculate('impots_directs', period = year)  # noqa F841
    reform_impo = reform_simulation.calculate('impots_directs', period = year) # noqa F841
