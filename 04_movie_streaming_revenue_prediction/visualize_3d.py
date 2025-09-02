import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movie_streaming_data.csv')

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

subscription_plans = df['subscription_plan'].unique()
colors = plt.cm.get_cmap('viridis', len(subscription_plans))

for i, plan in enumerate(subscription_plans):
    plan_data = df[df['subscription_plan'] == plan]
    ax.scatter(plan_data['time_spent_hours_per_week'], 
               plan_data['avg_watch_duration_minutes'], 
               plan_data['monthly_revenue_usd'], 
               label=plan, color=colors(i), alpha=0.7)

ax.set_xlabel('Time Spent (hours/week)')
ax.set_ylabel('Avg Watch Duration (minutes)')
ax.set_zlabel('Monthly Revenue (USD)')
ax.set_title('3D Plot of Time Spent, Avg Watch Duration, and Monthly Revenue by Subscription Plan')
ax.legend()
plt.show()
