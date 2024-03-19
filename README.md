# ISS Spotter Notifier

![ISS image](https://github.com/Addyk21/ISS-spotter-notifier/assets/121149505/097f8efb-0d5d-42ca-9916-ef9ff754bd30)

The International Space Station (ISS) zooms through space at an incredible speed of 28,165 kilometers per hour! Because it reflects sunlight, it's actually visible to the naked eye at night, making for a fascinating sight in the night sky.

## Overview

This script utilizes your location coordinates (latitude and longitude) as input to determine the proximity of the International Space Station (ISS) to your position. By incorporating the sunrise and sunset timings specific to your location, the script triggers a mail notification when it's nighttime, signaling the potential visibility of the ISS due to its light reflection.

## How it Works

1. It fetches your location using latitude and longitude.
2. It checks the ISS location using the Open Notify API.
3. It retrieves sunrise and sunset timings for your location using the Sunrise-Sunset API.
4. If the ISS is near and it's dark outside, you will receive a mail notification.

## API Used

1. [Sunrise-Sunset API](https://sunrise-sunset.org/api#limits) - Used to fetch sunrise and sunset timings.
2. [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) - Used to get the current ISS location.

## Modules Used

1. `smtplib` - For sending email notifications.
2. `requests` - For making HTTP requests to APIs.
3. `datetime` - For handling date and time.
4. `time` - For handling time-related operations.

## Usage

1. Clone the repository: `git clone https://github.com/Addyk21/ISS-spotter-notifier.git`
2. Run the script: `python iss_spotter.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
