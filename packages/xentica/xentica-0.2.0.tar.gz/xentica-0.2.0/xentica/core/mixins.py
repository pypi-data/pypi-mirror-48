"""
The collection of mixins to be used in core classes.

Would be interesting only if you are planning to hack into Xentica
core functionality.

"""
import inspect

import xentica.core.base
from xentica.core.exceptions import XenticaException

__all__ = ['BscaDetectorMixin', 'DimensionsMixin', ]


class BscaDetectorMixin:
    """
    Add a functionality to detect :class:`CellularAutomaton` class
    instances holding current class.

    """

    @property
    def bsca(self):
        """
        Get a :class:`CellularAutomaton` instance holding current class.

        The objects tree is scanned up to the top and the first
        instance found is returned.

        """
        frame = inspect.currentframe()
        while frame is not None:
            for local in frame.f_locals.values():
                if hasattr(local, "__get__"):
                    continue
                if isinstance(local, xentica.core.base.CellularAutomaton):
                    return local
            frame = frame.f_back
        raise XenticaException("BSCA not detected")

    @property
    def _holder_frame(self):
        """
        Get a frame of the class instance holding the current class.

        The objects tree is scanned up to the top and the first
        instance found is returned.

        """
        # As an option, we can detect base class by scanning inheritance tree:
        # inspect.getclasstree(inspect.getmro(type(self)))
        frame = inspect.currentframe().f_back.f_back.f_back
        while isinstance(frame.f_locals.get('self', ''), self.base_class):
            frame = frame.f_back
        return frame


class DimensionsMixin:
    """
    The base functionality for classes, operating on a number of dimensions.

    Adds ``dimensions`` property to a class, and checks it
    automatically over a list of allowed dimensions.

    """

    #: A list of integers, containing a supported dimensionality.
    #: You must set it manually for every class using :class:`DimensionsMixin`.
    supported_dimensions = []

    def __init__(self):
        """Initialize private variables."""
        self._dimensions = None

    def allowed_dimension(self, num_dim):
        """
        Test if a particular dimensionality is allowed.

        :param num_dim:
            The number of dimensions to test.

        :returns:
            Boolean value, either dimensionality is allowed or not.

        """
        return num_dim in self.supported_dimensions

    @property
    def dimensions(self):
        """Get a number of dimensions."""
        return self._dimensions

    @dimensions.setter
    def dimensions(self, num_dim):
        """Set a number of dimensions and check if it is allowed."""
        if not self.allowed_dimension(num_dim):
            msg = "%d-D %s is not supported."
            msg = msg % (num_dim, self.__class__.__name__)
            raise XenticaException(msg)
        self._dimensions = num_dim
