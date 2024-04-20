def trr(time):
    hour_entries = time['USTUNDE']
    day_entries = time['UWOCHENTAG']

    probabilities = time.groupby(['UWOCHENTAG','USTUNDE']).size()/len(time)
    time["Risk"] = time.apply(lambda x: probabilities[x['UWOCHENTAG']][x['USTUNDE']], axis=1)

    return time