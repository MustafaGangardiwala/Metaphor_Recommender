import os
import openai
from metaphor_python import Metaphor


#api
openai.api_key = os.getenv("OPENAI_API_KEY")
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))


def input_user_books():
    user_books = []
    print("Enter the details of the books you've read:")
    for _ in range(5):
        title = input("Enter the book title: ")
        user_books.append(title)
    return user_books

def add_read_book(self, book):
        self.read_books.append(book)

def get_recommendations(books):
    

    prompt = " ".join(books)
    SYSTEM_MESSAGE = "You are a recommendation system that recommends a topic based on users input. Just return the name of the article."

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ],
    )


    query = completion.choices[0].message.content
    search_response = metaphor.search(
        query, use_autoprompt=True
    )

    contents_result = search_response.get_contents()
    first_result = contents_result.contents[0]

    SYSTEM_MESSAGE = "You are a helpful assistant that can analyse the content of a webpage. Summarize the users input."

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": first_result.extract},
        ],
    )

    summary = completion.choices[0].message.content
    print(f"Summary for {first_result.title}: {summary}")


 
    

# Sample usage of the recommendation system
if __name__ == "__main__":
    user_books = input_user_books()

    recommendations = get_recommendations(user_books)