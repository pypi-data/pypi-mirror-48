[![PyPI Version](https://img.shields.io/pypi/v/tweety.svg)](https://pypi.org/project/tweety)
[![Coverage Status](https://coveralls.io/repos/github/santhoshse7en/tweety/badge.svg?branch=master)](https://coveralls.io/github/santhoshse7en/tweety?branch=master)
[![License](https://img.shields.io/pypi/l/tweety.svg)](https://pypi.python.org/pypi/tweety/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat)](https://santhoshse7en.github.io/tweety_doc)

# tweety

Twitter's API is annoying to work with, and has lots of limitations. tweety scrape all the tweets using python and selenium - No API rate limits. No restrictions. Extremely fast.

| Source         | Link                                         |
| ---            |  ---                                         |
| PyPI:          | https://pypi.org/project/tweety/             |
| Repository:    | https://santhoshse7en.github.io/tweety/      |
| Documentation: | https://santhoshse7en.github.io/tweety_doc/  |

**Average Tweets**

It appears you can ask for up to 25 pages around tweets reliably (~1200 tweets)

## Dependencies

* beautifulsoup4
* selenium
* chromedriver-binary
* vaderSentiment
* textblob
* pandas


## Dependencies Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following
```bash
pip install -r requirements.txt
```

## Usage

Download it by clicking the green download button here on Github. You only need to parse argument specific Twitter keyword.
```python
>>> from twitter.tweety import tweets
>>> tweety = tweets('Super Deluxe')
```

**Directory of tweety**

![dirt](https://user-images.githubusercontent.com/47944792/58116804-d3727b80-7c1a-11e9-9e2e-a675d98b8682.PNG)

## Output

```python
>>> print("Polarity Scores" + " : " + str(tweety.final_sentiment_scores))
```
![capture](https://user-images.githubusercontent.com/47944792/53886316-c3002b00-4045-11e9-8a56-10ef06275951.PNG)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
