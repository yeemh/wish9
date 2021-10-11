def solution(table, languages, preference):
    answer = ''
    lang_pref = {}
    for i in range(len(languages)):
        lang_pref[languages[i]] = preference[i]
        
    max_score = 0
    for job in table:
        score = 0
        job_lang = job.split(' ')
        for i in range(1,6):
            if job_lang[i] in lang_pref:
                score += lang_pref[job_lang[i]] * (6-i)
        if score > max_score:
            max_score = score
            answer = job_lang[0]
        elif score == max_score and job_lang[0] < answer:
            answer = job_lang[0]
            
    return answer