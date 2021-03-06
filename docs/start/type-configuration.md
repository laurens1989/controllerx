---
title: Controller types
layout: page
---

Each device supports a type of controller and this is what gives them the functionality over an entity. As for now, the two types of supported controllers are lights and media players.

Here you can check the specific parameters that each type of controller needs. Check the [configuration](configuration) page for the generic parameters.

## Light controller

This controller allows the devices to control light or group of lights. This allows you to:

- Turn on/off light(s)
- Toggle light(s)
- Manual increase/decrease of brightness and color
- Smooth increase/decrease (holding button) of brightness and color
- Color loop changing if the light supports xy color.

| key               | type                 | value                                           | description                                                                                                                                                                                              |
| ----------------- | -------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `light`\*         | string \| dictionary | `group.livingroom_lights` or `light.kitchen`    | The light (or group of lights) you want to control                                                                                                                                                       |
| `manual_steps`    | int                  | 10                                              | Number of steps to go from min to max when clicking. If the value is 2 with one click you will set the light to 50% and with another one to 100%.                                                        |
| `automatic_steps` | int                  | 10                                              | Number of steps to go from min to max when smoothing. If the value is 2 with one click you will set the light to 50% and with another one to 100%.                                                       |
| `smooth_power_on` | boolean              | False                                           | If `True` the associated light will be set to minimum brightness when brightness up is clicked or hold ad light is off.                                                                                  |
| `delay`           | int                  | [Controller specific](/controllerx/controllers) | Delay in milliseconds that takes between sending the instructions to the light (for the smooth functionality). Note that the maximum value is 1000 and if leaving to 0, you might get uncommon behavior. |

_\* Required fields_

Light dictionary for the `light` attribute:

| key          | type   | value           | description                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`\*     | string | `light.kitchen` | The light (or group of lights) you want to control                                                                                                                                                                                                                                                                                                                  |
| `color_mode` | string | `auto`          | This attribute can take `auto`, `xy_color` or `color_temp` as value. `auto` will check first if the light supports `xy_color` and then `color_temp`. `xy_color` will cicle through different colors infinitely. `color_temp` will change the color temperature attribute of the light. If a light supports both, user can pick which action wants for the light(s). |

_\* Required fields_

## Media player

This allows you to control media players. It supports volume, play/pause and skipping forward/backward the track.

| key              | type   | value                                                         | description                                                                                                                                                                 |
| ---------------- | ------ | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `media_player`\* | string | `group.livingroom_speakers` or `media_player.bedroom_speaker` | The media player (or group of media players) you want to control                                                                                                            |
| `volume_steps`   | int    | 10                                                            | Number of steps to go from min to max when clicking or holding. If the value is 2 with one click you will set the volume to 50% and with another one to 100%.               |
| `delay`          | int    | [Controller specific](/controllerx/controllers)               | Delay in milliseconds that takes between sending the volume up/down instructions. Note that the maximum value is 1000 and if leaving to 0, you might get uncommon behavior. |

_\* Required fields_
