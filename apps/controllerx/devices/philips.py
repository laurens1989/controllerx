from core import LightController, Stepper


class HueDimmerController(LightController):
    # Different states reported from the controller:
    # on-press, on-hold, on-hold-release, up-press, up-hold,
    # up-hold-release, down-press, down-hold, down-hold-release,
    # off-press, off-hold, off-hold-release

    def get_z2m_actions_mapping(self):
        return {
            "on-press": self.on,
            "on-hold": (self.hold, LightController.ATTRIBUTE_COLOR, Stepper.UP,),
            "on-hold-release": (self.release,),
            "up-press": (self.click, LightController.ATTRIBUTE_BRIGHTNESS, Stepper.UP,),
            "up-hold": (self.hold, LightController.ATTRIBUTE_BRIGHTNESS, Stepper.UP,),
            "up-hold-release": self.release,
            "down-press": (
                self.click,
                LightController.ATTRIBUTE_BRIGHTNESS,
                Stepper.DOWN,
            ),
            "down-hold": (
                self.hold,
                LightController.ATTRIBUTE_BRIGHTNESS,
                Stepper.DOWN,
            ),
            "down-hold-release": self.release,
            "off-press": self.off,
            "off-hold": (self.hold, LightController.ATTRIBUTE_COLOR, Stepper.DOWN,),
            "off-hold-release": self.release,
        }

    def get_deconz_actions_mapping(self):
        return {
            1000: self.on,
            1001: (self.hold, LightController.ATTRIBUTE_COLOR, Stepper.UP,),
            1003: self.release,
            2000: (self.click, LightController.ATTRIBUTE_BRIGHTNESS, Stepper.UP,),
            2001: (self.hold, LightController.ATTRIBUTE_BRIGHTNESS, Stepper.UP,),
            2003: self.release,
            3000: (self.click, LightController.ATTRIBUTE_BRIGHTNESS, Stepper.DOWN,),
            3001: (self.hold, LightController.ATTRIBUTE_BRIGHTNESS, Stepper.UP,),
            3003: self.release,
            4000: self.off,
            4001: (self.hold, LightController.ATTRIBUTE_COLOR, Stepper.DOWN,),
            4003: self.release,
        }

    def get_zha_actions_mapping(self):
        # return {"on": self.on, "off_with_effect": self.off}
        return None