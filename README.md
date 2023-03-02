# chatgpt-chatbot
Project for Computer Network course in Semester 4, HCMUS.

Chatbot trong discord: chạy file chatbot_discord.py.

Chatbot đang thử nghiệm trong terminal VSCode: chạy file chatbot_terminal.py để hiểu.
Miêu tả cho con bot này trong file chatbot_description.txt
Con này khác con trên ở chỗ nó nhớ được mình đã trò chuyện những gì, làm cho flow trò chuyện có tính liên tục (continuity). Tham khảo ở phần Continuity tại link này: https://pub.towardsai.net/build-chatgpt-like-chatbots-with-customized-knowledge-for-your-websites-using-simple-programming-f393206c6626
Cơ bản là sau mỗi lần người dùng nhập input, chatbot sẽ đưa ra response và lưu vào history. Sau mỗi lượt trò chuyện, prompt được cập nhật theo công thức: prompt = basic_description + history



UPDATED 17:52 2/3: cập nhật script và training data cho con bot.
description = script + train
prompt = description + history
