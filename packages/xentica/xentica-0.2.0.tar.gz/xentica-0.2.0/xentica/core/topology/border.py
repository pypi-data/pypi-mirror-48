"""
The collection of classes describing different types of field's borders.

All classes there are intended for use inside ``Topology`` for
``border`` class variable definition. They are also available via
:mod:`xentica.core` shortcut. The example::

    from xentica.core import CellularAutomaton, TorusBorder

    class MyCA(CellularAutomaton):
        class Topology:
            border = TorusBorder()
            # ...
        # ...

"""
import abc

from xentica.core.mixins import DimensionsMixin

__all__ = [
    'Border', 'WrappedBorder', 'GeneratedBorder',
    'TorusBorder', 'StaticBorder',
]


class Border(DimensionsMixin):
    """
    The base class for all types of borders.

    You should not inherit your borders directly from this class, use
    either :class:`WrappedBorder` or :class:`GeneratedBorder` base
    subclasses instead.

    """

    def __init__(self):
        """Initialize common things for all borders."""
        self.topology = None
        super(Border, self).__init__()


class WrappedBorder(Border):
    """
    The base class for borders that wraps the field into different manifolds.

    For correct behavior, you should implement :meth:`wrap_coords` method.

    See the detailed description below.

    """

    @abc.abstractmethod
    def wrap_coords(self, coord_prefix):
        """
        Generate C code to translate off-board coordinates to on-board ones.

        This is an abstract method, you must implement it in
        :class:`WrappedBorder` subclasses.

        :param coord_prefix:
            The prefix for variables containing the cell's coordinates.

        """


class GeneratedBorder(Border):
    """
    The base class for borders that generates states of the off-board cells.

    For correct behavior, you should implement :meth:`off_board_state` method.

    See the detailed description below.

    """

    @abc.abstractmethod
    def off_board_state(self, coord_prefix):
        """
        Generate C code to obtain off-board cell's state.

        This is an abstract method, you must implement it in
        :class:`GeneratedBorder` subclasses.

        :param coord_prefix:
            The prefix for variables containing the cell's coordinates.

        """


class TorusBorder(WrappedBorder):
    """
    Wraps the entire field into N-torus manifold.

    This is the most common type of border, allowing you to generate
    seamless tiles for wallpapers.

    """

    #: Any number of dimentions is supported, 100 is just to limit your
    #: hyperspatial hunger.
    supported_dimensions = list(range(1, 100))

    def wrap_coords(self, coord_prefix):
        """
        Implement coordinates wrapping to torus.

        See :meth:`WrappedBorder.wrap_coords` for details.

        """
        code = ""
        for i in range(self.dimensions):
            code += "{x}{i} = ({x}{i} + {w}{i}) % {w}{i};\n".format(
                x=coord_prefix, i=i,
                w=self.topology.lattice.width_prefix
            )
        return code


class StaticBorder(GeneratedBorder):
    """
    Generates a static value for every off-board cell.

    This is acting like your field is surrounded by cells with the
    same pre-defined state.

    The default is just an empty (zero) state.

    """

    supported_dimensions = list(range(1, 100))

    def __init__(self, value=0):
        """
        Store the static value.

        :param value:
            A static value to be used for every off-board cell.

        """
        self._value = value
        super(StaticBorder, self).__init__()

    def off_board_state(self, coord_prefix):
        """
        Impement off-board cells' values obtaining.

        See :meth:`GeneratedBorder.off_board_state` for details.

        """
        return str(self._value)
