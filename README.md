## Home Assistant Custom Component: Luncha I Mjärdevi

[![GitHub Release][releases-shield]][releases]
![Project Stage][project-stage-shield]
[![issues-shield]](issues)
[![License][license-shield]](LICENSE.md)

[![Buy me a coffee][buymeacoffee-shield]][buymeacoffee]

This custom component will create sensors for what is being served at the restaurants in and around Mjärdevi Science Park in Linköping, Sweden.
The sensors are compatible with the [Skolmat Lovelace card](https://github.com/Kaptensanders/skolmat-card) by [Kaptensanders](https://github.com/Kaptensanders)

You will need a free API key to the [Luncha I Mjärdevi](https://lunchaimjardevi.com/) API. You can get that by emailing me at luncha@popeen.com

I have started the progress of getting this repo included in the default HACS library but for now you have to add it to your HACS using [these instructions](https://hacs.xyz/docs/faq/custom_repositories/)

After installing the integration using HACS and restarting your server you simply configure the sensors by clicking the button below or by going to Devices & Services and adding it from there.

[![add-integration-shield]][add-integration]

[releases-shield]: https://img.shields.io/github/release/popeen/Home-Assistant-Custom-Component-Luncha-I-Mjardevi.svg
[releases]: https://github.com/popeen/Home-Assistant-Custom-Component-Luncha-I-Mjardevi/releases
[project-stage-shield]: https://img.shields.io/badge/project%20stage-ready%20for%20use-green.svg
[issues-shield]: https://img.shields.io/github/issues-raw/popeen/Home-Assistant-Custom-Component-Luncha-I-Mjardevi.svg
[license-shield]: https://img.shields.io/github/license/popeen/Home-Assistant-Custom-Component-Luncha-I-Mjardevi.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg
[hacs]: https://github.com/custom-components/hacs
[buymeacoffee-shield]: https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg
[buymeacoffee]: https://www.buymeacoffee.com/popeen
[add-integration-shield]: https://my.home-assistant.io/badges/config_flow_start.svg
[add-integration]: https://my.home-assistant.io/redirect/config_flow_start/?domain=lunchaimjardevi
