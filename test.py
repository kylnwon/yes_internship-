import csv 

class to_do_list_item(): 
    task = ""
    due_date = "" # dates will be in format of YYYY-MM-DD to make sorting easier (separted by dashes) 
    assignee = ""
    prio = False # True means in pgoress etc. 
    status = "" # in progress, not started or finished

    def __init__(self, task = "", due_date = "", assignee = "", prio = False) -> None:
        """ Default values for string values are empty string, and false for prio because fields are optional"""
        self.task = task 
        self.due_date = due_date
        self.assignee = assignee
        self.prio = prio 

    """ Functions that allow for changing of fields, can also can reset using to_do_list_item.x = X"""
    def change_task(self, task): 
        self.task = task 

    def change_due_date(self, due_date): 
        self.due_date = due_date

    def change_assignee(self, assignee): 
        self.assignee = assignee

    def change_status(self, status): 
        self.status = status 

class to_do_list(): 
    title = ""
    owner = ""
    items = [] 
    tags = [] 

    def __init__(self, title, owner) -> None:
        self.title = title 
        self.owner = owner

    """Allows you to add tdlist item to items and set default tag to empty list"""
    def add_td(self, item): 
        self.items.append(item)
        self.tags.append([])

def merge_two_lists(todo1, todo2): 
    # make dictionary with key being the date, and the value being the todo_list_item 
    """
    Code creates two dictionaries mapping due dates to todo list items for each lsit, each 
    value will be a list of all the values with that todo date

    list of dates is compiled and sorted, then each todo list item assigned to that date will be appended 
    to a new todlist object's item field and returned 
    """
    td1s = todo1.items
    td2s = todo2.items

    td1_dates = [td.due_date for td in td1s] 
    td2_dates = [td.due_date for td in td2s] 

    td1_dict = {} 
    td2_dict = {} 
    
    for i in range(len(td1s)): 
        # accounts for there being multiple todo items with the same due_date 
        if td1_dates[i] in td1_dict: 
            td1_dict[td1_dates[i]] += td1s[i]
        else: 
            td1_dict[td1_dates[i]] = [td1s[i]]

        if td2_dates[i] in td2_dict: 
            td1_dict[td2_dates[i]] += td2s[i]
        else: 
            td1_dict[td2_dates[i]] = [td2s[i]]
    
    td_dates = td1_dates + td2_dates
    td_dates.sort() 
    
    ans = []
    for date in td_dates: 
        if date in td1_dates: 
            for todo in td1_dates[date]: 
                ans.append(todo) 
            td1_dates.pop(date) 
        else: 
            for todo in td2_dates[date]: 
                ans.append(todo) 
            td2_dates.pop(date) 
        
    res = to_do_list("NA", "NA", ans)
    return res

def in_range(td_list, start_date, end_date): 
    tds = td_list.items
    td_dates = [td.due_date for td in tds] 

    res = [] 
    for date in td_dates: 
        if start_date <= date and end_date >= date: 
            res.append(date) 
    
    print(res)

    
"""
Takes in argument filter in all caps 
"""
def td_filter(td_list, filter): 
    tds = td_list.items
    res = []

    if filter == "DATE": 
        td_dates = [td.due_date for td in tds] 
        for i in range(len(tds)):   
            if td_dates[i] != "": 
                res.append(tds[i])       
    elif filter == "PRIO": 
        td_prios = [td.prio for td in tds]
        for i in range(len(tds)):   
            if td_prios [i] == False: 
                res.append(tds[i]) 
    elif filter == "ASSIGNED": 
        td_as = [td.assignee for td in tds] 
        for i in range(len(tds)):   
            if td_as [i] != "": 
                res.append(tds[i]) 
    else: 
        print("Error occured in parsing filter") #invalid filter type possibly not in all CAPS? 
    print(res) 

def add(file, td_list):
    # assume each line is a new todo list object 
    # in order of task, due_date, assignee, prio 

    #before 
    print(td_list.items)

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='-')
        for row in reader: 
            fields = row.split('-')
            td = to_do_list_item(task = fields[0], due_date = fields[1], asignee = fields[2], prio = fields[3])
            td_list.items.append(td)
    
    #after
    print(td_list.items)


"""
For hard problem, I'm gonna create a new field in td_list that is list of the tags each td_item has 
They will all be intilaied to an empty list at first 
"""

def tagger(td_list, td_item, tag): 
    tds = td_list.items
    
    for i in range(len(tds)):
        # found matching td_item you want to add tag to 
        if (tds[i].task == td_item.task) and (tds[i].prio == td_item.prio) and ((tds[i].assignee == td_item.assignee)) and (
            (tds[i].assignee == td_item.assignee)): 
            td_list.tags[i] += tag

def group_tags(td_list, tags): 
    res = [] 
    for i in range(td_list.tags): 
        tag_count = len(tags)
        temp = 0
        for tag in tags: 
            if tag in td_list.tags[i]: 
                temp += 1

        # have to make sure all the tags match and there are enough/not too many tags
        if temp == tag_count: 
            res.append(td_list.items[i])

    return res
    

    
