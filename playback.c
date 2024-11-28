def playback(input_text):
    return '...'.join(input_text.split())

if __name__ == "__main__":
    user_input = input()
    print(playback(user_input))
