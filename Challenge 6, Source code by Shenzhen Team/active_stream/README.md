# Active learning support for targeted Twitter stream

Our group did some experiments during the SDG summer school.
We ended up doing some experiments on Google Dialogflow. But Dialogflow requires a google account to access the online data.

The code included in Github is to track tweets about specific topics by tracking the keywords we are interested in. 


## About

The Twitter streaming API allows us to track tweets about a specific topic by tracking user-defined keywords. All tweets that contain a keyword can be accessed. Keywords allow for crude adjustments of precision/recall tradeoffs. We build a dataset (WBS_SDG.xlsx) including all (or the most useful) keywords a priori.


This system is aimed to build a streaming interface that allows the user to
obtain a fine tuned stream that maximizes the number of relevant tweets
from the stream.

Given a set of user selected seed keywords,
an initial stream is produced. The active learning component classifies tweets
as relevant or not and concurrently presents tweets to the user for manual
annotation. Only tweets that the system is most uncertain about are selected for
manual annotation. A second component proposes new keywords based on
co-occurence in the tweet text. 



## Dependencies

* See `conda_environment.yml` for all dependencies in the conda package manager format
* English language model for spaCy (`$ python -m spacy download en`)
* Mongodb (listening on `localhost:27017` which is default setting when
    installing mongodb)

## Run

Put your twitter credentials in a file named `credentials.py` of the 
following format:
```javascript
credentials = {"coll_1": {
        "access_token": "...",
        "access_token_secret": "...",
        "consumer_secret": "...",
        "consumer_key": "...",
    }
}
```

Start the backend with:
```bash
python app.py
```

Monitor status with:
```bash
tail -f debug.log
```

Then open a browser and navigate to:
```bach
localhost:5000
```
