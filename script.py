from groq import Groq

groq_api_key = open('GROQ_API_KEY.txt',mode='r').readline()

client = Groq(
    api_key = groq_api_key,
)

print('Hey there! Tell me the things you have to get done and the amount of time they each take. Once you are done, say stop.\n')

starting_time = input('What time do you want to start your to-do list?\n')

breaks = input('Do you want short breaks in between? Y/N\n')
if breaks=="Y":
    breaks = 'short breaks'
else:
    breaks = 'no breaks'
    
to_do_list = []
task_count = 1
while True:
    task = input(f'What is task {task_count} you have to get done?\n').lower()
    if task == 'stop':
        break
    else:
        time = input('How many hours do you need to do the task?\n')
        to_do_list.append(f'Task: {task}, Time (in hours): {time}')
        task_count += 1

prompt = f"Create me a full-day schedule with {breaks} in between tasks. Besides the tasks, include ordinary things a school student would do from morning to night. I want to start at {starting_time}. Give me just the schedule and no filler text. This is the list of things I need to get done and the amount of time they will each take: {to_do_list}. Don't write anything in bold."
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
)

schedule_count = open('schedule_count.txt',mode='r')
current_schedule_id = int(schedule_count.readline())

new_schedule = open(f'Schedules\\schedule_{current_schedule_id}.txt', mode='w')
new_schedule.write(chat_completion.choices[0].message.content)

new_schedule_count = current_schedule_id + 1
schedule_count = open('schedule_count.txt',mode='w')
schedule_count.write(str(new_schedule_count))