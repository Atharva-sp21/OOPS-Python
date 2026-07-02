# Data Versioning using DVC
Data Ingestion -> Data Preprocessing -> Feature Engineering -> Feature Selection -> Model Training -> Model evaluation
Each of these components are a fancy word for a module/ python file, where each python file has classes and methods, and all these classes are imported in the main.py and the pipeline is run
Now each pipeline is dynamic, eg. Data ingestion ka kaam hai ki ek MongoDB se data ingest karna, every module has an artifact(output for each module)
Now suppose you experiment with some new method in data ingestion which changes the pipeline in general, because of which our metrics change, now how do we rollback( suppose our new result was worse than the previous one )

Conclusion: We don't have a concrete solution to anythign, so we keep experimenting, after every component we have changes, so to change every save of each component, the concept of data versioning arose.

Why not use GIT? -> we use DVC along with it which saves the data versions ( cause data is HUGE in size which exceeds GIT's storage)


## HOW(THEORY)?
- You visited a temple, rules: your wallet, phone can't be taken inside and even shoes, so the temple has a counter where you can deposit this, but they don't allow you to keep shoes there, there is a different counter for it. Suppose you have the responsibility to collect from 20 different people, there is some ambiquity since you might mix up. So counters started giving coupons to fix this problem which maps to the respect person and their belongings. (id->belongings)
- Now think of Git and DVC, Git says that i will take care of the versioning of your code, i will track your code but the data with respect to it will be taken care by DVC. But how will we know which data is corresponding which change in github. So, DVC handles that which handles a token. eg. V1 data ka ek unique ID milega from DVC, so we commit ID in github too, now suppose V2 data ka unique ID i2 hai then we commit github that.
- In future when we rollback we will get the ID and then map it to that corresponding version of data.