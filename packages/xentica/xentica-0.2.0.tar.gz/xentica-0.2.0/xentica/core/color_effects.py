"""
The collection of decorators for the ``color()`` method, each CA model
should have.

The method should be decorated by one of the classes below, otherwise
the correct model behavior will not be guaranteed.

All decorators are get the ``(red, green, blue)`` tuple from
``color()`` method, then process it to create some color effect.

A minimal example::

    from xentica import core
    from xentica.core import color_effects

    class MyCA(core.CellularAutomaton):

        state = core.IntegerProperty(max_val=1)

        # ...

        @color_effects.MovingAverage
        def color(self):
            red = self.main.state * 255
            green = self.main.state * 255
            blue = self.main.state * 255
            return (red, green, blue)

"""
from xentica.core.variables import Constant
from xentica.core.mixins import BscaDetectorMixin

__all__ = ['ColorEffect', 'MovingAverage', ]


class ColorEffect(BscaDetectorMixin):
    """
    The base class for other color effects.

    You may also use it as a standalone color effect decorator, it just
    doing nothing, storing the calculated RGB value directly.

    To create your own class inherited from :class:`ColorEffect`, you
    should override ``__call__`` method, and place a code of the color
    processing into ``self.effect``. The code should process values
    of ``new_r``, ``new_g``, ``new_b`` variables and store the result
    back to them.

    An example::

        class MyEffect(ColorEffect):

            def __call__(self, *args):
                self.effect = "new_r += 20;"
                self.effect += "new_g += 15;"
                self.effect += "new_b += 10;"
                return super(MyEffect, self).__call__(*args)

    """

    def __init__(self, func):
        """Initialize base attributes."""
        self.func = func
        self.effect = ""

    def __call__(self):
        """
        Implement the color decorator.

        Sibling classes should override this method, and return
        ``super`` result, like shown in the example above.

        """
        red, green, blue = self.func(self.bsca)
        code = """
            int new_r = %s;
            int new_g = %s;
            int new_b = %s;
            %s
            col[i] = make_int3(new_r, new_g, new_b);
        """ % (red, green, blue, self.effect)
        self.bsca.append_code(code)


class MovingAverage(ColorEffect):
    """
    Apply the moving average to each color channel separately.

    With this effect, 3 additional settings are available for you in
    ``Experiment`` classes:

    fade_in
        The maximum delta by which a channel could
        *increase* its value in a single timestep.

    fade_out
        The maximum delta by which a channel could
        *decrease* its value in a single timestep.

    smooth_factor
        The divisor for two previous settings, to make
        the effect even smoother.

    """

    def __call__(self):
        """Implement the effect."""
        if not hasattr(self.bsca, "fade_in"):
            self.bsca.fade_in = 255
        if not hasattr(self.bsca, "fade_out"):
            self.bsca.fade_out = 255
        if not hasattr(self.bsca, "smooth_factor"):
            self.bsca.smooth_factor = 1
        self.bsca.define_constant(Constant("FADE_IN", self.bsca.fade_in))
        self.bsca.define_constant(Constant("FADE_OUT", self.bsca.fade_out))
        self.bsca.define_constant(Constant("SMOOTH_FACTOR",
                                           self.bsca.smooth_factor))
        self.effect = """
            new_r *= SMOOTH_FACTOR;
            new_g *= SMOOTH_FACTOR;
            new_b *= SMOOTH_FACTOR;
            int3 old_col = col[i];
            new_r = max(min(new_r, old_col.x + FADE_IN),
                        old_col.x - FADE_OUT);
            new_g = max(min(new_g, old_col.y + FADE_IN),
                        old_col.y - FADE_OUT);
            new_b = max(min(new_b, old_col.z + FADE_IN),
                        old_col.z - FADE_OUT);
        """
        return super(MovingAverage, self).__call__()
