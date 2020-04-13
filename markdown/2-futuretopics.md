# Future topics for articles

## Overview of things I plan to (eventually) write about, a growing list

---

Fenno Vermeij, April 13, 2020

---

In this list, I will... list... the topics I plan to write about. Keep in mind I will add topics to this list as I come up with them. No promises or anything, but just to act as inspiration for myself.

### Iterrows vs itertuples

The advantages of `itertuples` are well known, but I still can't find a blog that shows the functional differences between `iterrows` and `itertuples`, such as the fact that column names containing whitespaces are renamed with `itertuples`, and dtypes possibly changing. For just the timing differences, [I found this blog](https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06) to be very helpful.

### Geodata using Python/R, both feature and raster data, and explaining geo-joins

I'm far from the first to write about geodata, but I still think I can write a short and sweet summary of the tools in R/Python, specifically for data scientists, to easily work with geodata. Also, I am fascinated by geo-joins, using geo-indexes, and how much faster they are than brute-force vertical lookups, so I think it would be a nice challenge to visualize those.

### Quantile Regression, both Meinshausen and Tilted loss

A topic that is known, but not super well known as it (in my opinion) should be. Quantiles can be very useful in regression: instead of predicting a single number, we can predict a 95% confidence interval. This costs extra training time, but little to no programming or extra data is required. The main two methods I'm aware of are the Meinshausen method, specifically for random forests, and the tilted loss method, that can be used for anything else. Also, there is a fun trick the ranger package uses to massively speed up the Meinshausen method, at the cost of performance, which I think is not as well known as it should be.

### Azure pipelines

This is more of a 'my personal experience' idea: I have written couple of python-specific azure pipelines. I am certainly not an expert on this, so it would be more of a 'getting started with some simple stuff' blog.

### Personal learning project - deploying sklearn model as Python/Java/C/Go

This isn't something I have experience with, but I think it would be really cool to dive in some of these languages I last used in university, and build a machine learning model in them. Then, do some benchmarking, and see if I can even deploy some of them to web services, for instance using Azure Functions, and benchmark them there as well. This would be an interesting comparison to see some of the advantages of transpiling SKLearn models, as well as just being a cool and interesting personal project.

Ther are some interesting approaches and code examples [in this stackoverflow post](https://stackoverflow.com/questions/12738827/how-can-i-call-scikit-learn-classifiers-from-java)

### Summarizing my findings from studying for AZ-204

I almost achieved the AZ-204 certificate, and I could write some of my summaries and learnings there. For now, I have collected my notes [on this Github repository](https://github.com/fennovj/azure-notes), but it's by no means a summary or collection of most interesting topics. After AZ-204, I plan to go for either AZ-400, DP-201, or perhaps DP-100, so I could do the same for those.
