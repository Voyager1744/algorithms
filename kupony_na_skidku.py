def find_maximum_discount(n, m, k, costs, discounts, applicable_coupons):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            for coupon in applicable_coupons[i]:
                if j >= coupon:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - coupon] + discounts[
                        coupon])

    return dp[n][k]


n, m, k = map(int, input().split())
costs = list(map(int, input().split()))
discounts = [0] * (m + 1)
applicable_coupons = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    coupon_info = list(map(int, input().split()))
    discount = coupon_info[0]
    discounts[i] = discount
    for j in range(1, len(coupon_info)):
        applicable_coupons[coupon_info[j]].append(i)

chosen_coupons = find_maximum_discount(
    n, m, k, costs, discounts, applicable_coupons)
print(chosen_coupons)
