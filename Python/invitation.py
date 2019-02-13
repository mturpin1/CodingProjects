guest_name = input('What is the name of the guest? ')
party_name = input('What is the name of the party? ')
party_date = input('What is the date of the party? ')
party_time = input('What is the time of the party? ')
RSVP_date = input('What is the latest RSVP date? ')
host_name = input('What is the name of the host of the party? ')
print(
    '''
    
    Dear %s,

    You are cordially invited to the %s
    on %s at %s. Please RSVP no later than
    %s.

    Sincerely,

    %s
    ''' %(guest_name, party_name, party_date, party_time, RSVP_date, host_name))
