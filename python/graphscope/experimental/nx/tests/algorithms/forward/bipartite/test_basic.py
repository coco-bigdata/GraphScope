import networkx.algorithms.bipartite.tests.test_basic
import pytest

from graphscope.experimental.nx.utils.compat import import_as_graphscope_nx

import_as_graphscope_nx(networkx.algorithms.bipartite.tests.test_basic,
                        decorators=pytest.mark.usefixtures("graphscope_session"))
