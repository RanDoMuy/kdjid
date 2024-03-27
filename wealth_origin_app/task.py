from .models import User

def increase_profit_balance():
    instances = User.objects.exclude(trade_status= "INACTIVE")
    
    for instance in instances:
        if instance.trading_plan == "STARTER":
            profit_increase = 50
            instance.profit_balance += profit_increase
            instance.save()
            
        if instance.trading_plan == "BRONZE":
            profit_increase = 100
            instance.profit_balance += profit_increase
            instance.save()
            

        if instance.trading_plan == "SILVER":
            profit_increase = 200
            instance.profit_balance += profit_increase
            instance.save()

        if instance.trading_plan == "GOLD":
            profit_increase = 300
            instance.profit_balance += profit_increase
            instance.save()

        if instance.trading_plan == "DIAMOND":       
            profit_increase = 500
            instance.profit_balance += profit_increase
            instance.save()

        if instance.trading_plan == "PLATINUM":
            profit_increase = 1000
            instance.profit_balance += profit_increase
            instance.save()