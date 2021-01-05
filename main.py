# api key jjXzrkTRBJ209RpsumrqYuGn0
# api secret key L0aig9c6Se5RU5uGR1MRKmcWDgRQJW70BFp74Jln9q38pWL6iF
# bearer token AAAAAAAAAAAAAAAAAAAAADUlLQEAAAAA2S%2FvkqduomEnc84PvFPn5Nyh4Mg%3DEU5XxHfAIt0p2wdXaHvB7Lu8W7r5HHYW93AGltD2N3koUwsN7d
# access token key 16205995-A7fffhY0Ro0CFIvjhmHUlk41RuH2eXCZgksx3QJqC
# access token secret bWjB1HJgJIpJsTsdizs5TvZ2H7EU4zlJ1VrkidAJDV5ZC
# https://github.com/QuincyLarson/delete-tweets/blob/master/deletetweets.py
# https://www.freecodecamp.org/news/how-to-delete-your-past-tweets-in-bulk-and-for-free-save-yourself-from-your-past-self-f8844cdbda2/

import twitter

def delete(api):
    with open("tweets.csv") as file:
        count = 0

        #for each row, get tweet id and delete
        count += 1

    print("Deleted {} tweets!".format(count))

def main():
    # TODO use environment variables / .env file
    api = twitter.Api(
        consumer_key="",
        consumer_secret="",
        access_token_key="",
        access_token_secret=""
    )


if __name__ == "__main__":
    main()
