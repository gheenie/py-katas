
def years_of_growth(
    initial_population,
    target_population,
    growth_rate,
    net_migration
):
    if growth_rate == 0:
        return 'infinite'

    years_passed = 0

    while initial_population < target_population:
        initial_population *= 1 + growth_rate / 100
        initial_population += net_migration

        years_passed += 1
    
    return years_passed
