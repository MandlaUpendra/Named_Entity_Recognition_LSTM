import pandas as pd
import numpy as np
import spacy
from IPython.display import Image

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import yaml

from rouge_score import rouge_scorer

import locale
locale.getreferredencoding = lambda: "UTF-8"

with open("config.yaml","r") as file:
    config = yaml.safe_load(file)

summary_url = config['processing']['summary_source_url']
raw_url = config['processing']['raw_source_url']

summary = pd.read_csv(summary_url, encoding='iso-8859-1')
raw = pd.read_csv(raw_url, encoding='iso-8859-1')

raw = raw.rename(columns={'headlines':'summary'})
summary = summary[['headlines','text']].rename(columns={'headlines':'summary'})

df = pd.concat([raw, summary]).reset_index(drop=True)

summary.shape, raw.shape