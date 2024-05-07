import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    
    elif hour>=12 and hour <= 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am voice assistant of Computer Department. How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 20000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Welcome to KKW")
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            speak(results)

        elif 'marks' in query or 'rank' in query and 'open' in query:
            speak('Recalling the rank...')
            results = "The rank required is 12800 and below and percentile are 95 and above"
            speak(results)
        
        elif 'marks' in query or 'rank' in query and 'obc' in query:
            speak('Recalling the rank...')
            results = "The rank required is 15000 and below and percentile are 94 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'sc' in query:
            speak('Recalling the rank...')
            results = "The percentile are 88 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'st' in query:
            speak('Recalling the rank...')
            results = "The percentile are 84 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'tfws' in query:
            speak('Recalling the rank...')
            results = "The percentile are 98 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'ews' in query:
            speak('Recalling the rank...')
            results = "The percentile are 95 and above"
            speak(results)
    
        elif 'intake' in query or 'capacity' in query:
            speak('Recalling the capacity ...')
            results = "The Intake of Computer Department is 120"
            speak(results)

        elif 'documents required' in query and 'obc' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card, Allotment Letter, SSC and HSC Result,
            Domicile Certificate, Non-Creamy layer, Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'documents required' in query and 'sc' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card, Allotment Letter, SSC and HSC Result,
            Domicile Certificate, Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'documents required' in query and 'st' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card, Allotment Letter, SSC and HSC Result,
            Domicile Certificate, Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'documents required' in query and 'nt' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card,Allotment Letter, SSC and HSC Result,
            Domicile Certificate,Non-Creamy layer,Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'admission fee' in query and 'open' in query:
            speak('Calculating the fees')
            results = "148000"
            speak(results)

        elif 'admission fee' in query and ('obc' in query or 'ews' in query or 'ebc' in query):
            speak('Calculating the fees')
            results="Total fees for OBC or EWS or EBC is 80 thousand"
            speak(results)

        elif 'admission fee' in query and ('sc' in query or 'st' in query):
            speak('Calculating the fees')
            results="Total fees for SC and ST is 0 rupees"
            speak(results)

        elif 'admission fee' in query and 'tfws' in query:
            speak('Calculating the fees')
            results="Total fees for TFWS category is 18 thousand"
            speak(results)

        elif 'admission fee' in query and ('vjnt' in query or 'sbc' in query):
            speak('Calculating the fees')
            results="Total fees for VJNT is 18 thousand"
            speak(results)

        elif 'overview' in query:
            speak('''It was established in 1970 by the visionary leader Late Padma Shri   Karmaveer    Kakasaheb   Wagh   and our   responsibility is 
                  To be a   premier   institution that nurtures a legacy of academic excellence, character development and   civic responsibility.''')
            
        elif 'objective' in query:
            speak('''The objective of the K K Wagh Education Society is to provide quality education at 
                  an affordable cost. A quality culture has been developed in all the institutes.''')
            
        elif 'facilities' in query:
            speak('Every Facility is here right from Academic Facility to Hostel Services On which Facility should I highlight')

        elif 'Academic' in query:
            speak('''We Provides  Innovation Centre and Idea Lab , A proper Engineering Workshop , For Placement Preparation  Training & Placement Cell 
                   For Blooming Reading Culture A central Library with 2 Lakh plus books available''')
            
        elif 'Sports' in query:
            speak('''Special Playgrounds for Cricket , FootBall , Special Courts for BasketBall ,  Volleyball ,  Lawn Tennis , Well Equipped 
                  Gymnasieum , Table Tennis , Chess and Carrom Facility to develop their Interpersonal Skills''')

        elif 'Medical' in query:
            speak(''' K K W has dispensary in the campus named Karmaveer Dispensary. All on-campus staff and students have access to the medical facilities. 
                  Institute has a tie-up with Apollo Hospital and Sushrut Hospital and NDMVP Medical College.''')
            
        elif 'Transport' in query:
            speak('''The K K Wagh Education Society's educational institutions are well connected from all parts of Nashik district.
                  As traveling requires a lot of time and effort, the Karmaveer bus facility was launched in 2006 to meet the needs of students.
                  The department started with 3 buses and 150 students. At present 1465 students are taking advantage of the transport facility. ''')
            
        elif 'Hostel' in query:
            speak(''' In Boy’s hostel, 368 students are staying while in girl’s hostels 225 girls’ students are residing. 
                  These hostels are provided with two seated and three seated rooms and solar systems are installed to avail hot water for students.
                  All other facilities are provided in all rooms. 
                  The hostel is also provided with an Internet facility, Study room, Television and filtered water. ''')

        elif 'Package' in query:
            speak('''Average Package of computer department is about 5.97 LPA  Highest Package is  22 LPA No. of Students placed 
                  in Academic Year 2022 is 613''')

        elif 'Recruiters' in query or 'company' in query:
            speak('''Amdocs , BoschIT , Capgemini , Cognizant , Datamatics , Deolitte , IBM , Infosys , Nvidia , Oracle
                  Reliance Jio , Winjit , T C S and many more top IT recruiters''')

        elif "why you came to the world" in query:
            speak("Thanks to Gayatri. further It's a secret")

        else:
            speak("Sorry, I'm still learning. I don't know that yet.")