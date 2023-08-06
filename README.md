# BBC NEWS Summarizer with OpenAI GPT-3.5

![BBC NEWS Summarizer](https://ichef.bbci.co.uk/images/ic/1920xn/p09xtmrp.jpg)

This repository contains a NEWS summarizer for BBC.com using OpenAI GPT-3.5 with the OpenAI API key. The code takes the latest articles from BBC.com and provides a concise summary of each article using the power of GPT-3.5 language model.

## Getting Started

### Prerequisites

Before running the code, make sure you have the following installed:

- Python (version 3.6 or higher)
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/BBC-Summarizer.git
cd bbc_news_summarizer
```

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### API Key Setup

To use the OpenAI GPT-3.5 language model, you need an API key from OpenAI. Follow these steps to set up your API key:

1. Sign up or log in to your OpenAI account at [https://platform.openai.com/](https://platform.openai.com/).
2. Generate an API key from your dashboard.
3. Replace the `openai_api_key` variable in `run.py` with your actual API key:

```python
# Set your OpenAI API key here
openai_api_key = "YOUR_API_KEY"
```

### Running the Summarizer

To use the NEWS summarizer, follow these steps:

1. Make sure you have set up the API key as explained above.
2. Open the `run.py` file and find the `summarized` parameter. By default, it is set to `False`, which means it will provide a summary directly from BBC.com. To use GPT-3.5 for summarization, set `summarized = True`.

```python
# Set summarized to True for GPT-3.5 summarization
summarizer.get_articles(
    openai_api_key=openai_api_key, hours=5, body=False, summarized=True
)
```

3. Run the script:

```bash
python run.py
```

The summarizer will fetch the latest articles from BBC.com and either provide summaries using GPT-3.5 or display the original article based on the value of the `summarized` parameter.



## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

## Disclaimer

Please be aware that using the OpenAI API may incur costs, depending on your usage and subscription plan. Make sure to check the OpenAI website for the latest pricing information.

Please also note that this summarizer is designed for educational and personal use only. Respect the terms of service of BBC.com and OpenAI when using this tool.

---
Happy summarizing!
