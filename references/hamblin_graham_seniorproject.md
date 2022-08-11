# Project Proposal

### Personal Background

I have completed Math 425 (Applied Linear Regression), CSE 450 (Machine Learning), and am currently enrolled in Math 488 (Consulting).  Upon graduating in December, I hope to find work related to education or government projects and look forward to enrolling in a Master's program within the next two years.

Email: ham20052@byui.edu

### Project Background

Bot accounts and other spam have become an overwhelming presence on social media in the past year or so - particularly in the YouTube comments section.  While channels are able to block users from interacting with their posts, it has become impossible to maintain the quality of community interactions by manually reporting each incident.  Luckily, there are a handful of distinct features that we can use to identify and block spam accounts, which I plan to apply automatically through a chrome extension or similar product.  I will use selenium or the YouTube API to collect and classify comments from a variety of channels and video categories, which I can feed into a model or collection of specified rules to improve the accuracy with which spam is identified.

### Domain to Investigate

As part of collecting YouTube comments and details from their respective commenters, I will need to understand the html layout of the platform as well as how to edit or hide comments using javascript.  It may also be necessary for me to understand the controls and access given provided for channels to regulate content within their communities, as I only have experience as a viewer.

### Proposed Deliverables

Beyond building a model to detect spam, I hope to deploy a chrome extension to filter YouTube comments in real time.  Much like Google's safe-search preferences, I will provide users with an option to increase or decrease the filter's strictness for various types of content (profanity, violence, etc.).  As other deliverables, I will research the following topics and determine if and how they can be implemented in the final product: 

- Regular Expressions: Identify phone numbers, links, etc. that may be indicative of spam
- Natural Language Processing: interpret comments and flag content as directed by the user
- Computer Vision: detect violent or pornographic profile pictures as well as any image that may be used to impersonate another user.
