# Social Media Sentiment Analysis with PySpark

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

4. **Docker & Docker Compose** (Optional):
   - If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## **Project Structure**

```
SocialMediaSentimentAnalysis/
├── input/
│   ├── posts.csv
│   └── users.csv
├── outputs/
│   ├── hashtag_trends.csv
│   ├── engagement_by_age.csv
│   ├── sentiment_engagement.csv
│   └── top_verified_users.csv
├── src/
│   ├── task1_hashtag_trends.py
│   ├── task2_engagement_by_age.py
│   ├── task3_sentiment_vs_engagement.py
│   └── task4_top_verified_users.py
├── docker-compose.yml
└── README.md
```

## **Running the Analysis Tasks**

### **a. Running Locally**

1. **Navigate to the Project Directory**:
   ```bash
   cd SocialMediaSentimentAnalysis/
   ```

2. **Execute Each Task Using `spark-submit`**:
   ```bash
     spark-submit src/task1_hashtag_trends.py
     spark-submit src/task2_engagement_by_age.py
     spark-submit src/task3_sentiment_vs_engagement.py
     spark-submit src/task4_top_verified_users.py
   ```

3. **Verify the Outputs**:
   ```bash
   ls outputs/
   ```

### **b. Running with Docker (Optional)**

1. **Start the Spark Cluster**:
   ```bash
   docker-compose up -d
   ```

2. **Access the Spark Master Container**:
   ```bash
   docker exec -it spark-master bash
   ```

3. **Run PySpark Scripts**:
   ```bash
   spark-submit src/task1_hashtag_trends.py
   spark-submit src/task2_engagement_by_age.py
   spark-submit src/task3_sentiment_vs_engagement.py
   spark-submit src/task4_top_verified_users.py
   ```

## **Project Overview**

This project leverages Apache Spark's Structured APIs to perform a comprehensive social media sentiment analysis. By examining a dataset of social media posts, we extracted meaningful insights about user engagement, hashtag trends, and sentiment dynamics.

## **Detailed Analysis Results**

### 1. Hashtag Trends Analysis

**Top 10 Hashtags:**
| Hashtag    | Count |
|------------|-------|
| #UX        | 25    |
| #fail      | 25    |
| #cleanUI   | 24    |
| #design    | 24    |
| #love      | 22    |
| #bug       | 22    |
| #social    | 20    |
| #tech      | 16    |
| #AI        | 16    |
| #mood      | 12    |

**Key Observations:**
- Design and user experience (#UX, #cleanUI, #design) are prominent topics
- Technology-related hashtags (#tech, #AI) show significant presence
- Mix of positive (#love) and critical (#fail, #bug) hashtags

### 2. Engagement by Age Group

| Age Group | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Adult     | 77.33     | 25.48        |
| Teen      | 73.59     | 26.53        |
| Senior    | 69.10     | 22.65        |

**Key Insights:**
- Adults lead in average likes
- Teens show highest average retweets
- Seniors have slightly lower engagement metrics
- Relatively consistent engagement across age groups

### 3. Sentiment vs Engagement

| Sentiment   | Avg Likes | Avg Retweets |
|-------------|-----------|--------------|
| Negative    | 75.95     | 26.38        |
| Positive    | 73.38     | 19.48        |
| Neutral     | 68.31     | 28.78        |

**Surprising Findings:**
- Negative posts have highest average likes
- Neutral posts have highest average retweets
- Positive posts have lowest retweet count
- Suggests complexity of user engagement beyond simple sentiment

### 4. Top Verified Users by Reach

| Username        | Total Reach |
|-----------------|-------------|
| @social_queen   | 1,439       |
| @meme_lord      | 1,295       |
| @pixel_pusher   | 1,063       |
| @calm_mind      | 925         |

**Influencer Insights:**
- @social_queen leads with highest total reach
- Verified users show significant engagement
- Top 4 users demonstrate substantial social media impact

