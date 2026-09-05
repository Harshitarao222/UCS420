#Q1
import pandas as pd

roll_no = "1024170123"

last_two = roll_no[-2:]

categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

personalized_entries = []

for digit in last_two:
    d = int(digit)
    category = categories[d % 3]

    if category == "billing":
        entry = {
            "question": "how can i check my payment status",
            "answer": "You can check your payment status in the billing section.",
            "keywords": "payment status bill",
            "category": "billing"
        }

    elif category == "account":
        entry = {
            "question": "how do i update my registered mobile number",
            "answer": "Go to Account Settings and update your registered mobile number.",
            "keywords": "mobile number update",
            "category": "account"
        }

    else:
        entry = {
            "question": "where can i contact customer support",
            "answer": "You can contact customer support during working hours.",
            "keywords": "support contact help",
            "category": "general"
        }

    personalized_entries.append(entry)

all_entries = fixed_entries + personalized_entries

df = pd.DataFrame(all_entries)

print(df)

def score_query(query, df):
    query_words = query.lower().split()
    results = []

    for index, row in df.iterrows():
        keywords = row["keywords"].lower().split()
        score = 0

        for word in query_words:
            if word in keywords:
                score += 1

        if score > 0:
            results.append((index, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results


query = input("Enter your query: ")

results = score_query(query, df)

print("\nMatching entries:")

for index, score in results:
    print("Question:", df.loc[index, "question"])
    print("Answer:", df.loc[index, "answer"])
    print("Confidence:", score)

def same_category(category_name, df):
    return df[df["category"] == category_name]["question"]


category_name = personalized_entries[0]["category"]

print("\nQuestions in category:", category_name)
print(same_category(category_name, df))

entry_index = 0

new_keyword = input("Enter a new keyword: ")

df.loc[entry_index, "keywords"] = (
    df.loc[entry_index, "keywords"] + " " + new_keyword
)

filename = roll_no + "_faq_data.csv"

df.to_csv(filename, index=False)

print("\nUpdated DataFrame:")
print(df)

print("\nFile saved as:", filename)

category_count = df.groupby("category").size()

print("\nFAQ entries per category:")
print(category_count)


def score_query_with_ties(query, df):
    query_words = query.lower().split()
    scores = []

    for index, row in df.iterrows():
        keywords = row["keywords"].lower().split()
        score = 0

        for word in query_words:
            if word in keywords:
                score += 1

        if score > 0:
            scores.append((index, score))

    if len(scores) == 0:
        return []

    highest_score = max(score for index, score in scores)

    best_matches = []

    for index, score in scores:
        if score == highest_score:
            best_matches.append((index, score))

    return best_matches

query = "fee"

matches = score_query_with_ties(query, df)

print("\nTie demonstration:")
print("Query:", query)

for index, score in matches:
    print("Question:", df.loc[index, "question"])
    print("Answer:", df.loc[index, "answer"])
    print("Score:", score)


query = "password"

matches = score_query_with_ties(query, df)

print("\nNon-tie demonstration:")
print("Query:", query)

for index, score in matches:
    print("Question:", df.loc[index, "question"])
    print("Answer:", df.loc[index, "answer"])
    print("Score:", score)
    