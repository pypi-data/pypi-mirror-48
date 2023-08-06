# RIP Counter

Count vote on [https://www.referendum.interieur.gouv.fr/consultation_publique/8](https://www.referendum.interieur.gouv.fr/consultation_publique/8).

RIP Counter can use multiple captcha solvers:

- A manual solver where an operator needs to enter the captcha.
- An automatic solver using captchanet: [https://github.com/hadim/captchanet](https://github.com/hadim/captchanet).
  - *The current version of CaptchaNet (version 4) has a sucess rate of about 33% per captcha images.*

## Usage

### Docker

Using Docker is easier because you don't have to setup a Python environment:

```bash
export RIP_COUNTER_COOKIE_NAME="incap_ses_531_2043128"
export RIP_COUNTER_COOKIE_VALUE="3V4yAmW8fmLvJA7G7n5eBxRbHV0AAAAAmB4th13GWlgFvUSW5IyFbw=="
export RIP_COUNTER_DATA_DIR="<PATH_TO DATA_DIRECTORY>"
docker run -ti --rm \
           -v $RIP_COUNTER_DATA_DIR:/data \
           -e RIP_COUNTER_COOKIE_NAME \
           -e RIP_COUNTER_COOKIE_VALUE \
           hadim/rip-counter
```

- The process usually takes a few hours.
- Once it's done, `$RIP_COUNTER_DATA_DIR` should contains your data as CSV files.
- The last output of the script (`scrap-my-rip`) will also gives you the number of votes.
- `scrap-my-rip` will generate a bunch of files:
  - `scraper.log`: Log of the scraper.
  - `all_urls.json`: Contains URLs of all the scraped pages ordered by the first two letters. It is used to restore scraping (this file is removed after each scraping session).
  - `2019-07-04_data.csv`: A table generated at each run. It contains one vote per row.
  - `master_data.csv`: A summary containing the sum of votes for each date.
  - `data_by_communes.csv`: Vote count for each day of scrap and also each communes. Non French communes (without INSEE code) are also present in the file.

You can also build the Docker image locally and use docker-compose:

```bash
git clone https://github.com/hadim/rip-counter.git
cd rip-counter/
docker-compose build

export RIP_COUNTER_COOKIE_NAME="incap_ses_531_2043128"
export RIP_COUNTER_COOKIE_VALUE="3V4yAmW8fmLvJA7G7n5eBxRbHV0AAAAAmB4th13GWlgFvUSW5IyFbw=="
export RIP_COUNTER_DATA_DIR="<PATH_TO DATA_DIRECTORY>"
docker-compose run rip

docker-compose rm -f
```

### Local

You first need to create a Python environment. We encourage you to use the [Anconda distribution](https://www.anaconda.com/distribution/):

```bash
conda create -n rip_env
conda activate rip_env
conda env update -f environment.yml

# Then install libraries not available in conda-forge.
pip install --no-deps -U tensorflow-datasets tensorflow_metadata tensorboard tensorflow-estimator
pip install --no-deps -U tensorflow==2.0.0-beta1
```

Now install the `rip-counter` library:

```bash
conda activate rip_env
pip install https://github.com/hadim/rip-counter/archive/master.zip
```

Then you can start counting:

```bash
export RIP_COUNTER_COOKIE_NAME="incap_ses_531_2043128"
export RIP_COUNTER_COOKIE_VALUE="3V4yAmW8fmLvJA7G7n5eBxRbHV0AAAAAmB4th13GWlgFvUSW5IyFbw=="
export RIP_COUNTER_DATA_DIR="<PATH_TO DATA_DIRECTORY>"
scrap-my-rip
```

## Telegram Bot

`rip-counter` also has a Telegram bot, that you can run on a server. Then you cn control scraping daily using a few simple commandes you send to the bot.

- You first need to create a bot and get the token associated to it at [https://core.telegram.org/bots#6-botfather](https://core.telegram.org/bots#6-botfather).

- Then get your user id associated to your personal account so the bot will talk to you and only to you. Talk to [@myidbot](https://telegram.me/myidbot) to get your user id.

- Start the bot using Docker:

```bash
export RIP_COUNTER_BOT_TOKEN="<TELEGRAM_BOT_TOKEN>"
# Use comma to allow multiple users.
export RIP_COUNTER_BOT_ALLOWED_USERS="99999,2827364"
export RIP_COUNTER_DATA_DIR="<PATH_TO DATA_DIRECTORY>"

docker run -ti --rm \
           -v $RIP_COUNTER_DATA_DIR:/data \
           -e RIP_COUNTER_BOT_TOKEN \
           -e RIP_COUNTER_BOT_ALLOWED_USERS \
           hadim/rip-counter
```

The available commands are:

- `/start`: Start a scraping session.
- `/stop`: Stop a scraping session.
- `/status`: Check if a scraping session is currently running.
- `/log`: Display the lst 10 lines of the log.
- `/set_cookie`: Set Incapsula cookie name:

```bash
/set_cookie incap_ses_1226_2043128 WtIoIix+tSfAQxu1tqADEfhmI10AAAAArK81JEbV3YaB02Y7AUcxaw==
```

## API

You can also use `rip-counter` in a Python script:

```python
import os
import rip_counter

rip_data_dir = '<PATH TO DATA DIR>'

os.environ['RIP_COUNTER_COOKIE_NAME'] = 'incap_ses_303_2043128'
os.environ['RIP_COUNTER_COOKIE_VALUE'] = "M+otKL5POk133ss9Jnk0BExMH10AAAAAyM8+JLZw1q3nfwIZMFZehA=="

captcha_solver = rip_counter.CaptchaNetSolver(preload_model=True)
scraper = rip_counter.RIPScraper(captcha_solver=captcha_solver, save_dir=rip_data_dir,
                                 max_captcha_try=20, shuffle_urls=False)

# Scrap !
await scraper.scrap(batch_size=64, show_progress=True, _test_mode=False)

# Post process data
data = scraper.process_data()

print(data.loc[:, data.columns.str.startswith('vote_count')].sum())
```

## License

Under BSD license. See [LICENSE](LICENSE).

## Authors

- Hadrien Mary <hadrien.mary@gmail.com>
