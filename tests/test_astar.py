from lab6_intelligent_search.services.search_service import find_route


def test_astar_route():
    result = find_route('A', 'F')

    # A-C-F y A-B-E-F cuestan 7: ambas son rutas óptimas
    assert result['path'] in (['A', 'C', 'F'], ['A', 'B', 'E', 'F'])
    assert result['cost'] == 7
