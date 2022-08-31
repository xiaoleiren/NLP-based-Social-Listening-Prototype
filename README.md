# NLP-based-Social-Listening-Prototype
---------------------
![image](https://github.com/xiaoleiren/NLP-based-Social-Listening-Prototype/blob/main/SDG%20SC%20Images/SDG_W4_PRE-v0.4.pptx.png)

Using social listening approaches to understand impact of Global Fund activities on raising awareness efforts around HIV, TB and Malaria

Team members: Hyungmin Lee, Chen-Chun Hsia, Syuanying Lin, Jiaxi Zhang,
Coach: Xiaolei Ren

SDG Summer School,
University of Geneva,
2022

### Structure 
```

|-- Source code
|   |-- SDG_GF_Nigeria
|   |-- active_stream
|   |-- ...
|   |-- app.py
|
|-- SDG SC Images
|   |-- ...
|
|-- Dataset
|   |-- SDG.xlsx
| 
|-- Google Dialog Flow
|   |-- online platform
|
|-- LICENSE
|-- README.md
```


Dataset: https://docs.google.com/spreadsheets/d/1dylCpyONAl_SojM-mvg4MSWjAM4G6rVRNuwIbBgcuIE/edit#gid=1228678965

Google dialog flow：https://dialogflow.cloud.google.com/#/agent/sdg-gf-nigeria-2-t9fi/intents

Twitter API: 
https://developer.twitter.com/en/docs/twitter-api/annotations/overview

https://developer.twitter.com/en/docs/tutorials/post-processing-twitter-data-with-the-google-cloud-platform

A campaign by WHO to raise the awareness of global antimicrobial resistance:

https://www.who.int/news-room/events/detail/2020/11/18/default-calendar/world-antimicrobial-awareness-week-2020

World Antimicrobial Awareness Week:

https://www.theglobalfund.org/en/news/2022/2022-03-22-global-fund-calls-for-renewed-urgency-in-fight-to-end-tb/


---------------------
Over the millennia, infectious diseases have changed and evolved again, causing mankind great suffering. The "Big Three" infectious diseases, which include tuberculosis, malaria, and HIV/AIDS, are among the most deadly infections in the world since they cause the most infections and fatalities each year (Makam et al., 2021). The Global Fund has been working and making contributions to the battle against these three fatal diseases in light of these frightening circumstances. 
Programs for education and public awareness can be used to make a group of people aware of these diseases. Posters, radio or television programs, as well as online social media platforms, are all possible formats for this kind of endeavor. One of the most significant and effective methods of prevention is raising public awareness. to convey important preventative messages to your target demographic (youth, adults, or children) and motivate them to take precautionary measures against certain diseases (Start, 2000).

The study of public awareness and impact deals with human behavior and is influenced by a variety of elements, including culture, family, state, and education. Measurement and evaluation of the results of awareness-raising efforts in a timely, efficient, and systematic manner continue to be difficult. Currently, there is no platform to use a social listening approach to understand the impact of GF activities on HIV, TB and malaria awareness efforts. Through systematic investigation, we propose to use natural language processing models to analyze social big data to understand the impact of GF activities more deeply using social listening methods, and we expect that our model can provide some inspiration and help to solve this challenge and move the field forward.

Solution
 
Methodology: It is a challenge to effectively and systematically assess the effects of awareness-raising initiatives. Through systematic investigation, we propose to use natural language processing models to analyze social big data to understand the impact of GF activities more deeply using social listening methods.

---------------------
![image](https://github.com/xiaoleiren/NLP-based-Social-Listening-Prototype/blob/main/SDG%20SC%20Images/SDG_W4_PRE-v0.4.pptx-3.png)

Details:
---------------------
We have looked through the WHY and WHAT of the custom datasets, HOW on starting social big data analysis with real world examples relavant to GF and lastly the roadmaps.

Why 
- Accessible social big data analytics on the internet were made for marketing analysis that  the language model is focused on commercial and general domains. Therefore, GF couldn’t sense important and relevant keywords that GF wants to detect. 

What
- Thus, It is necessary for GF to make custom dataset that fits GF’s needs. In this project, our team selected three sample intervention topics to address the whole methodology; accessible HIV testing, continuous TB treatment, and Malaria prevention with the mosquito nets. Each of the topic gains the highest statistical attentions in The Data Explorer, GF’s data platform.

How
- We firstly handpicked entity-synonyms list from GF’s reports, news, and twitters relevant to the three topics. With the initial entities, we filtered relevant twitter post to further expand the entity list and cleanse the post to use it as corpus. Then we use the entity and the corpus to train NLP model. In result, the model can detect relevant and similar keywords and understand the contents of the post and categorize it into one of three topics.
- To closely measure how much the twitter post is relevant to the intervention topic, post-processing model with scoring algorithm is necessary. It often uses the frequency of the relevant keywords appeared in the post however it can widely varies according to the requirements and this project doesn’t covers it as it requires major engagements of GF.

Data Roadmap
- The entity and the corpus made for this project can expand its usage to improving GF employee’s work efficiency by applying it to in-company search engine, build chatbots to instantly respond requests from different time zone, and connects the chatbot with BI, RPA, ERP to automate working process using natural langauge. Plus, It can also be used to franchise its innovation to other NGO’s who wants to make similar innovation efficiently by reusing the common corpus and changing the entity list more relevant to their domain.


For the source code, we used our own dataset, based on the Twitter API, to train a number of different NLP models, and after training and testing, unfrtunately, we found that these models were not effective. So after further study, we used an NLP model provided in an online platform - google dialog flow cloud to finish this project.

https://dialogflow.cloud.google.com/#/agent/sdg-gf-nigeria-2-t9fi/intents

dialogflow, if you want to try to use our prototype tool, please feel free to email me, I will add your gmail to get access to it.

Contact
-------------

If you have good idea or want to contribute to this project, please feel free to reach out to us either by creating issues on GitHub or sending emails to xiaolei.ren@uta.edu. Many thanks : )

