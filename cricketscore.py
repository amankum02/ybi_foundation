import pandas as pd
data={
    'Player':['Rohit Sharma','KL Rahul', 'Virat Kohli','Shreyas Iyyer','Hardik Pandya','Axar Patel','Ravindra Jadeja','Kuldeep yadav','Jasprit Bumrah','Mohammad Siraj','Mohammad Shami'],
    'Runs':[45, 38, 75, 25,55, 50, 15, 10, 0, 5, 0],
    'Wickets':[0,0,0,0,1,0,2,3,1,2,4],
    'Balls Faced':[38,35,70,20,50,45,12,8,2,4,1],
    'Balls Bowled':[0,0,0,0,4,0,10,10,10,10,10]
}
match_data= pd.DataFrame(data)

#calculate total runs
total_runs=match_data['Runs'].sum()

#calculate Batting Average
match_data['Batting Average']= match_data['Runs']/ (match_data['Runs']-match_data['Balls Faced'])

#calculate Bowling Strike Rate
bowlers= match_data[match_data['Balls Bowled']>0]
bowlers['Bowling Strike Rate']= bowlers['Balls Bowled']/bowlers['Wickets']

#calculate top run scorer
top_scorer=match_data.loc[match_data["Runs"].idxmax(),'Player']

#calculate top wicket taker
top_wicket=bowlers.loc[bowlers['Wickets'].idxmax(),'Player']

#calculate player points
match_data['Points']=(match_data['Runs']//10)+(match_data['Wickets']*20)

def choice():
    print("1.Total Run\n2.Batting Average\n3.Bowling Strike Rate\n4.Top Scorer\n5.Top Wicket Taker\n6.Players Points\n7.Exit")
    ch = int(input('Enter the choice: '))
    if ch == 1:
        print('Total Runs:', total_runs)
        print('====================================================')
        choice()

    elif ch == 2:
        print('Batting Average:\n', match_data['Player', 'Batting Average'])
        print('====================================================')
        choice()

    elif ch == 3:
        print('Bowling Strike Rate:\n', bowlers[['Player', 'Bowling Strike Rate']])
        print('====================================================')
        choice()

    elif ch == 4:
        print('Top Run Scorer: ', top_scorer)
        print('====================================================')
        choice()

    elif ch == 5:
        print('Top Wicket taker: ', top_wicket)
        print('====================================================')
        choice()

    elif ch == 6:
        print('Player Points:\n', match_data[['Player', 'Points']])
        print('====================================================')
        choice()

    elif ch == 7:
        exit(0)
choice()

