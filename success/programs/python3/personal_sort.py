"""def birthdayCakeCandles(ar):
    a= ar[:]
    b=0
    c=1
    b = max(a)
    a.remove(b)
    for i in a:
        if max(a)==b:
            c+=1
            a.remove(max(a))
    print(c)
ar = [4,4,1,33,341,5,777,87,56,455,3546,7677,8879,56536,656,777,56536,1,56536]
birthdayCakeCandles(ar)
"""
#a = [1201,4,1,33,341,5,777,87,56,455,3546,7677,8879,56536,656,777,56536,1,56536]
a = [3412, 1440, 2253, 2718, 2997, 3229, 1022, 3691, 3533, 2032, 2407, 1334, 2936, 2026, 2575, 532, 2655, 2839, 2423, 2311, 4630, 2974, 1423, 3085, 3089, 1611, 3628, 1249, 1790, 3985, 582, 1325, 1443, 547, 3914, 4109, 2307, 1298, 1853, 3812,
 1831, 4267, 1416, 2729, 2402, 3539, 2975, 2021, 2415, 769, 3991, 1675, 3424, 865, 2395, 3940, 1691, 1147, 1360, 518, 1625, 4251, 2427, 4540, 1986, 1251, 1936, 3583, 3865, 3203, 2474, 2927, 4079, 545, 3185, 1553, 1322, 3579, 4553, 2481, 4678,
4519, 2210, 3023, 1963, 1039, 1463, 4350, 2466, 4236, 2121, 2389, 2878, 2517, 4037, 569, 3763, 2638, 4632, 1225, 723, 2079, 4546, 3105, 912, 1794, 776, 3454, 3785, 888, 2441, 4573, 1809, 2305, 2082, 1922, 2051, 4081, 4204, 971, 3027, 1994, 
4122, 4473, 2956, 1952, 3793, 2475, 3151, 4624, 4325, 2155, 3324, 2934, 3612, 600, 2524, 1248, 2295, 4231, 3665, 2339, 3663, 3258, 1364, 3226, 2764, 1120, 2871, 2259, 4664, 1846, 2296, 3119, 954, 1395, 968, 3733, 4570, 4480, 4145, 625, 1462,
1168, 2899, 3295, 640, 638, 3961, 2952, 530, 4662, 3936, 2855, 3544, 3990, 4489, 2174, 1119, 4149, 1958, 562, 2811, 2779, 1058, 1488, 4558, 4198, 1296, 1605, 892, 4118, 646, 824, 503, 907, 2523, 1641, 739, 1948, 3980, 3930, 3967, 2363,
2767, 1047, 1801, 1715, 1171, 939, 2909, 3890, 1151, 985, 4197, 682, 3683, 2111, 3595, 2568, 4035, 2445, 1427, 2144, 1110, 2613, 4454, 1479, 890, 1478, 767, 3274, 2050, 3077, 4516, 592, 1821, 3916, 1563, 2491, 4069, 2159, 3194, 3603, 3594, 
3862, 2969, 4481, 1802, 616, 3692, 1921, 2097, 1828, 1810, 1338, 4053, 3323, 1413, 4471, 3090, 1552, 2099, 4638, 4447, 1545, 2712, 2840, 4658, 3576, 3510, 2615, 1707, 2530, 3094, 2823, 2771, 752, 4201, 1217, 1907, 788, 4307, 1035, 2460, 3792,
3479, 846, 1169, 1684, 1126, 1356, 3306, 861, 2759, 1841, 1816, 2015, 3493, 3886, 3103, 2518, 1768, 2746, 1987, 534, 2600, 3188, 2949, 4320, 2225, 2713, 533, 4358, 3933, 1310, 3680, 3520, 1164, 2699, 3573, 1036, 2651, 3708, 590, 1509, 4523, 
2550, 3232, 3578, 1257, 2734, 3047, 970, 581, 1726, 3165, 1817, 821, 4498, 2814, 3682, 2980, 1470, 2012, 3969, 1068, 2213, 3065, 2693, 2654, 2094, 1293, 3819, 2181, 4495, 2566, 1199, 2957, 2894, 1621, 2688, 2090, 1583, 2967, 1620, 3292, 3270, 1454, 1474, 2016, 2826, 1866, 2786, 3797, 2023, 2177, 2495, 4302, 3092, 4462, 3679, 2691, 1593, 2137, 1420, 3910, 622, 749, 1274, 2810, 515, 1283, 849, 1351, 1233, 3813, 3553, 1191, 1379, 1417, 2807, 4367, 879, 1967, 1441, 1864, 3637, 783, 1096, 3540, 2046, 1601, 3875, 1057, 1066, 601, 1868, 2081, 2556, 1571, 2576, 529, 2697, 3410, 3350, 1105, 3926, 3563, 2635, 4338, 2768, 1184, 1609, 3825, 2490, 1447, 2185, 1452, 1014, 738, 3277, 589, 4040, 3433, 4299, 3938, 1247, 2701, 2336, 2020, 1886, 3396, 3322, 4123, 1946, 686, 2102, 2868, 1803, 3142, 1670, 3840, 827, 4368, 3381, 4682, 1400, 2951, 3283, 2841, 2084, 4381, 3039, 4421, 574, 1702, 2954, 602, 1860, 4527, 2477, 2538, 1706, 1511, 2789, 2930, 2502, 1214, 4107, 3821, 1876, 560, 1404, 4352, 4635, 3867, 3749, 527, 4515, 3269, 3066, 1579, 536, 784, 1113, 1835, 3993, 3388, 3725, 3931, 2925, 2091, 4435, 3982, 4619, 4239, 1932, 4675, 2123, 1497, 1928, 4097, 3178, 514, 2022, 3452, 774, 1046, 3349, 1737, 4230, 4469, 1747, 965, 4125, 3574, 1143, 2017, 721, 4121, 4374, 3496, 3123, 4566, 4102, 4258, 2992, 1431, 2984, 1830, 3303, 3972, 4348, 3197, 2900, 2692, 650, 2065, 4578, 889, 2880, 3545, 2647, 3182, 856, 1642, 1673, 580, 664, 2966, 1926, 1333, 565, 3405, 2351, 1281, 3799, 3086, 3686, 2345, 2135, 2299, 3289, 3494, 3308, 4005, 631, 1514, 3245, 3537, 3618, 3075, 1320, 2818, 1152, 1272, 4163, 4592, 3114, 4534, 1944, 3468, 4311, 4683, 1767, 2031, 4235, 2705, 3170, 3437, 1965, 3795, 1539, 3911, 2928, 4518, 3364, 1748, 1203, 3186, 1069, 628, 4321, 4194, 1531, 1934, 4622, 561, 3095, 3428, 3048, 2294, 1905, 2218, 1308, 3655, 637, 2126, 3827, 1402, 1721, 1562, 2327, 2876, 4605, 2112, 1158, 1888, 3604, 1879, 4333, 1969, 3482, 3756, 1503, 607, 2676, 3191, 2241, 4067, 1465, 4328, 4395, 3217, 2709, 2269, 2424, 1358, 3754, 3820, 1919, 1018, 2765, 3330, 2897, 666, 4211, 1761, 3949, 4490, 3588, 1585, 2739, 2113, 3055, 4400, 714, 4084, 3695, 3994, 3728, 1731, 1701, 1460, 1973, 2917, 908, 3995, 753, 710, 499, 4243, 1582, 4684, 2089, 3507, 3116, 4322, 1535, 2853, 1710, 3830, 1912, 2244, 2760, 3846, 2776, 4190, 634, 2306, 924, 2039, 2077, 4499, 1316, 3653, 1198, 2256, 1457, 4503, 2579, 3878, 701, 522, 2834, 1495, 4195, 1774, 1725, 1775, 1295, 3501, 3515, 4434, 2348, 2748, 2349, 3702, 3892, 4247, 2929, 3377, 2527, 2710, 3623, 1507, 3803, 2049, 1284, 712, 3081, 3131, 1327, 2036, 1469, 2640, 630, 4387, 4353, 695, 1714, 3591, 2725, 4668, 795, 4009, 4070, 1869, 3953, 2716, 1398, 1505, 2512, 550, 747, 1037, 4128, 756, 3919, 1812, 1367, 1163, 2184, 2276, 1218, 4509, 3956, 1650, 4418, 2106, 504, 2642, 3272, 546, 2141, 2946, 3889, 3360, 1508, 3764, 2193, 657, 3362, 4433, 2948, 1288, 4337, 1444, 4297, 3659, 3421, 4209, 3254, 3724, 633, 1896, 1050, 2569, 755, 4300, 4277, 586, 2270, 1280, 2815, 2191, 4136, 556, 2999, 1382, 3134, 4246, 1204, 2221, 763, 2858, 661, 1656, 1045, 3002, 1405, 1929, 3816, 982, 3363, 910, 4002, 1231, 1981, 3589, 2882, 2467, 3394, 2601, 2404, 1892, 3345, 2380, 1877, 2499, 3472, 1166, 595, 1616, 2047, 4240, 2754, 1309, 4041, 4550, 2803, 700, 2564, 4476, 2938, 1170, 2009, 1739, 3569, 1867, 3418, 1286, 3109, 975, 3413, 1010, 3843, 573, 3607, 3298, 1751, 2511, 3943, 823, 2536, 761, 2489, 1658, 1648, 1667, 3554, 4393, 1740, 508, 1106, 1778, 2639, 4443, 539, 3672, 2724, 3609, 3915, 1822, 1903, 2400, 3332, 537, 1902, 1663, 4467, 3384, 2920, 2574, 1968, 519, 578, 1727, 1854, 692, 4463, 3872, 1148, 2271, 3860, 1193, 1374, 2429, 3069, 3527, 1195, 1461, 2194, 3934, 4162, 2000, 2662, 2379, 3287, 1501, 2301, 2649, 4420, 2073, 1056, 991, 2607, 1924, 673, 4153, 4456, 1301, 1787, 4491, 3684, 1337, 1920, 662, 4072, 2565, 1303, 2870, 3688, 2308, 964, 1174, 3668, 3837, 684, 3832, 1265, 2631, 733, 1782, 4044, 809, 2470, 4030, 4226, 1425, 2606, 2611, 1336, 3198, 1471, 1052, 2666, 2641, 2153, 1458, 4652, 4394, 1683, 3171, 1438, 2741, 4058, 2584, 4103, 1692, 4631, 1634, 995, 575, 4429, 1970, 1935, 3535, 2175, 789, 1626, 2346, 4318, 3351, 1765, 1278, 4051, 4207, 1703, 3921, 3382, 3389, 3486, 4484, 882, 4437, 4133, 2798, 3524, 3671, 1436, 3810, 2406, 4357, 2338, 4685, 1389, 3586, 3240, 3160, 4494, 703, 3876, 1811, 1139, 3266, 4312, 3301, 1377, 4572, 2508, 2033, 3903, 3004, 1743, 2862, 4060, 1142, 674, 1665, 762, 1159, 3893, 2199, 875, 3190, 2044, 2223, 745, 1393, 2660, 2412, 921, 1121, 3773, 3251, 2167, 3877, 1763, 2820, 3140, 1434, 977, 2120, 992, 4203, 698, 4089, 4115, 4082, 685, 2922, 1578, 2356, 2011, 2204, 1114, 3492, 4465, 4244, 1729, 1855, 2469, 1092, 765, 3438, 1760, 2867, 4093, 656, 831, 4180, 743, 1182, 1491, 1819, 3015, 1664, 1548, 1668, 2589, 3551, 3593, 1895, 3490, 3918, 2268, 4234, 1290, 4210, 1654, 2101, 1044, 3341, 3984, 655, 1008, 4617, 4384, 3596, 834, 1424, 3470, 2988, 2667, 3640, 2190, 1957, 2473, 1187, 4569, 2700, 1640, 3740, 3704, 4217, 3534, 3422, 2599, 1652, 862, 1519, 4634, 3005, 1359, 3948, 1153, 1770, 1078, 3531, 4414, 2783, 3873, 1264, 1776, 3181, 1480, 2377, 4616, 897, 1486, 1749, 4594, 3929, 538, 3748, 1526, 3201, 1910, 1686, 4506, 4583, 4399, 729, 2388, 3485, 2069, 2059, 2192, 4200, 2875, 3834, 3321, 1544, 797, 4222, 2458, 2187, 4151, 3689, 1371, 1577, 2312, 3473, 2238, 4114, 2196, 572, 1960, 2543, 1122, 996, 3928, 3040, 4665, 781, 2808, 2972, 676, 3782, 4199, 1728, 3971, 2588, 898, 2231, 2664, 2453, 1077, 3831, 2286, 1297, 2727, 2421, 3158, 3857, 1433, 3497, 3162, 4334, 3305, 4268, 3036, 1759, 3411, 4430, 1789, 2737, 670, 4054, 4052, 2289, 3121, 3835, 4022, 1791, 4416, 4039, 4485, 1041, 2953, 3032, 3786, 1378, 4598, 1202, 2881, 1005, 3372, 3460, 2169, 1956, 955, 4557, 1477, 2696, 2371, 2095, 1261, 1236, 2685, 2145, 3811, 2559, 3667, 1824, 1681, 919, 4604, 2626, 2529, 1341, 3215, 2328, 3660, 1602, 4500, 1878, 1102, 4008, 3110, 523, 1676, 1580, 2819, 3018, 2409, 1610, 1598, 3558, 3526, 1962, 3606, 4233, 3096, 4216, 571, 3755, 2220, 2784, 2250, 2281, 2822, 1659, 4146, 2506, 4171, 1246, 2989, 1542, 3212, 1518, 3111, 2521, 4510, 4552, 2330, 3148, 1011, 2827, 705, 4458, 4000, 932, 1797, 1985, 513, 3365, 1915, 2726, 2963, 507, 3143, 2373, 1536, 1339, 1175, 2905, 2903, 4155, 2796, 4439, 3262, 3700, 720, 3214, 3757, 1370, 3041, 2873, 3932, 1844, 2316, 876, 3800, 4273, 3962, 1219, 3722, 3814, 2154, 3024, 1386, 2227, 2128, 2182, 1720, 1185, 4161, 4193, 2595, 1437, 3690, 3769, 770, 894, 1990, 4326, 1696, 1687, 1473, 3605, 1565, 2848, 563, 2720, 3347, 1340, 3078, 3071, 3343, 771, 3200, 790, 2817, 1572, 2665, 693, 1521, 3774, 2926, 3489, 1455, 1306, 1766, 841, 1753, 2103, 2581, 4409, 1529, 626, 815, 1698, 1220, 3242, 2464, 4087, 3173, 930, 3711, 1344, 3884, 4173, 2283, 813, 1408, 4264, 3505, 2526, 1033, 4262, 4417, 4655, 1240, 597, 2304, 2119, 744, 1523, 1160, 987, 2677, 3037, 4036, 1335, 1704, 3502, 544, 4019, 4647, 541, 1365, 1515, 2960, 956, 2659, 3009, 2837, 2249, 1695, 4185, 2719, 2513, 3144, 2755, 3180, 3736, 990, 1300, 4237, 4127, 3136, 2452, 1504, 2498, 4441, 1449, 3601, 1061, 1961, 1034, 4629, 4351, 2983, 2340, 4091, 2577, 4347, 4603, 2892, 4681, 2879, 4150, 3042, 928, 3157, 3509, 2869, 842, 4033, 2684, 1636, 4582, 3152, 3044, 1466, 3175, 3098, 3329, 715, 599, 3518, 1222, 4623, 1104, 903, 4372, 3030, 3788, 2630, 1722, 610, 4580, 1772, 1815, 2413, 1111, 2043, 2537, 1023, 3645, 4660, 899, 3256, 1132, 4260, 1212, 2072, 2911, 619, 511, 1814, 1546, 4196, 3922, 2916, 1260, 4181, 786, 1451, 4650, 3946, 4545, 4404, 1738, 3255, 918, 4023, 2706, 3038, 1029, 2551, 3218, 2134, 1534, 1613, 4275, 2736, 1421, 3352, 4561, 2359, 832, 3522, 4182, 4601, 4184, 3431, 2235, 1173, 3415, 1510, 736, 555, 2558, 3480, 647, 3318, 3495, 4112, 2671, 2354, 2003, 3548, 1685, 3279, 2675, 2381, 1127, 1808, 3761, 2070, 2782, 3448, 1063, 1328, 746, 2440, 4004, 4382, 4046, 2519, 1361, 1138, 2661, 2910, 2010, 3570, 1007, 4585, 1015, 3838, 2838, 4059, 4380, 2505, 3054, 1324, 3390, 4531, 1394, 718, 1662, 4524, 4383, 3124, 1622, 3565, 2525, 2054, 2885, 4577, 2114, 3739, 2650, 3249, 2058, 1410, 3714, 4538, 4130, 792, 1388, 4218, 2801, 4654, 2497, 726, 3600, 4187, 3439, 4141, 598, 806, 4511, 2545, 1414, 1723, 2315, 4562, 1532, 3235, 4677, 893, 4034, 3598, 1525, 3894, 1757, 1415, 2573, 1925, 1971, 2086, 1677, 3020, 2849, 690, 1916, 916, 1373, 2092, 727, 4478, 3122, 4063, 2790, 3941, 3636, 3469, 4410, 3726, 4228, 867, 2652, 677, 1629, 3286, 1285, 509, 2130, 1750, 2237, 4202, 750, 2695, 3064, 3458, 3271, 3135, 629, 3204, 937, 1141, 2290, 1490, 2232, 2890, 1678, 2459, 3973, 3836, 1671, 2571, 1475, 3432, 3267, 2670, 3917, 4296, 2598, 1899, 613, 3585, 2510, 2287, 857, 1842, 4361, 4581, 3231, 3650, 1201, 2372, 2401, 521, 4407, 1697, 2234, 2325, 4249, 3179, 644, 2034, 4551, 927, 3833, 1603, 1100, 4227, 2751, 3696, 552, 4024, 4189, 1396, 4006, 886, 2645, 1099, 3459, 2602, 1381, 3735, 1062, 1861, 4653, 3616, 1206, 2263, 3223, 1070, 4279, 2515, 1764, 4263, 848, 2024, 1780, 1679, 3963, 1453, 4284, 3016, 3861, 4365, 1038, 2813, 885, 4555, 3117, 4625, 1262, 829, 3643, 4095, 810, 2461, 3648, 3849, 4642, 1448, 3599, 3912, 615, 999, 2944, 3759, 2002, 3608, 1849, 2799, 3294, 1133, 1384, 1009, 1354, 3113, 1533, 4670, 3678, 787, 4671, 2093, 4398, 3753, 3108, 947, 1275, 683, 4389, 2151, 1560, 4229, 4140, 4323, 2136, 1955, 1006, 4068, 2769, 902, 2384, 1933, 4656, 3652, 3580, 962, 1785, 1330, 3744, 3519, 2943, 3061, 4466, 3025, 3699, 3099, 3354, 2971, 3657, 1234, 4340, 2366, 1079, 1134, 4100, 1628, 2854, 1745, 1053, 1820, 526, 940, 2766, 3257, 2528, 4219, 4270, 3252, 2516, 4116, 993, 4292, 4031, 2332, 960, 3130, 4191, 2919, 3705, 535, 3166, 1883, 1112, 4265, 4281, 980, 3694, 531, 2753, 4016, 1551, 3620, 4502, 724, 3500, 4131, 2449, 2376, 2852, 2539, 2637, 4679, 3013, 651, 3312, 1917, 2923, 3715, 2468, 2750, 1180, 4007, 1982, 3012, 4214, 642, 3359, 1116, 3487, 3342, 1312, 4108, 1346, 3543, 1468, 4633, 4304, 3859, 4377, 2970, 3285, 2987, 2678, 4178, 1874, 2738, 3371, 2447, 3221, 3383, 2127, 3964, 2291, 2554, 3567, 1945, 3750, 2211, 3631, 1840, 549, 2108, 2985, 1909, 4106, 3425, 3826, 3670, 1064, 3564, 1618, 3455, 2648, 4602, 4317, 665, 1215, 1051, 2179, 3778, 540, 520, 611, 4280, 3632, 2198, 1244, 2578, 620, 1682, 3309, 3387, 2763, 2448, 1635, 2163, 4487, 3720, 2282, 2350, 2038, 833, 2995, 3801, 671, 3145, 1211, 3988, 2331, 2066, 3435, 4285, 1392, 1383, 1380, 4335, 4521, 2369, 3779, 1758, 777, 3234, 1385, 4301, 2668, 1326, 591, 2863, 779, 1317, 1418, 3752, 2243, 922, 3391, 1754, 3864, 3654, 3050, 4314, 2105, 3649, 1190, 4073, 1600, 3474, 2329, 1718, 2057, 973, 4274, 735, 725, 4614, 2378, 1266, 2958, 2628, 945, 3374, 2230, 734, 2942, 2950, 2657, 1564, 826, 1108, 1543, 567, 548, 3824, 3125, 4676, 1586, 2794, 4482, 3966, 2722, 3150, 2319, 2273, 4330, 1606, 2104, 4468, 1612, 3996, 3007, 3073, 3146, 3045, 3615, 884, 1777, 2548, 989, 2353, 4448, 3512, 4062, 2907, 2621, 4212, 3403, 4608, 4442, 1472, 4094, 2280, 2939, 2644, 773, 4135, 2314, 1555, 1735, 4045, 1694, 2375, 2785, 3815, 3247, 2266, 1311, 2247, 3026, 3844, 3817, 4119, 1223, 3997, 2634, 4220, 3466, 2681, 1762, 3348, 1355, 3290, 3998, 2663, 4282, 2156, 2968, 2496, 808, 2170, 1834, 3888, 838, 1467, 1172, 658, 4269, 4295, 3525, 2770, 2252, 1130, 2893, 1157, 2604, 652, 917, 4241, 1798, 4452, 1871, 4554, 3504, 3451, 3957, 2188, 3056, 926, 2590, 4472, 873, 1406, 2643, 3765, 2493, 608, 2096, 1183, 3874, 3738, 1599, 2616, 1623, 2222, 1993, 3572, 1146, 2805, 3850, 2618, 2707, 1352, 3829, 3033, 3398, 782, 737, 3552, 1712, 4064, 524, 3562, 3051, 4276, 4370, 2157, 1065, 2669, 1498, 2843, 1115, 4278, 2886, 2795, 1323, 1575, 2947, 972, 3737, 4639, 2208, 1059, 844, 3053, 2704, 3427, 4666, 1645, 697, 2224, 1700, 1644, 2933, 618, 1894, 3419, 3313, 1724, 4451, 4568, 1481, 3781, 2851, 3052, 4003, 1996, 3476, 2416, 4250, 1329, 4428, 2758, 3772, 943, 3333, 4648, 3101, 1075, 1901, 1607, 949, 4379, 2457, 1235, 4129, 1397, 3141, 2993, 2322, 4332, 4636, 2792, 798, 3635, 1913, 3189, 4423, 1347, 2411, 3895, 1783, 2791, 1277, 3881, 1221, 3001, 3808, 3443, 4018, 4360, 979, 4288, 3300, 3376, 1617, 2075, 3082, 3902, 2990, 3358, 2653, 3856, 1387, 2323, 845, 4156, 4111, 566, 2430, 2715, 3230, 1071, 3806, 4444, 4517, 2672, 988, 694, 2341, 2442, 3154, 2504, 2703, 3311, 1097, 4406, 3467, 1744, 2382, 4014, 1988, 2456, 859, 2228, 1615, 500, 978, 1027, 2258, 1269, 4186, 713, 3818, 3244, 4376, 3674, 2913, 1891, 1103, 3923, 3022, 696, 2812, 967, 3955, 1947, 850, 1357, 793, 1412, 1974, 3717, 981, 3378, 2207, 2683, 4497, 1422, 4606, 4425, 3063, 3770, 4117, 4615, 2895, 2142, 2945, 2450, 3981, 1321, 3783, 803, 4541, 4574, 2494, 1937, 1556, 1426, 1088, 4667, 2609, 1773, 2045, 2555, 660, 3937, 1390, 593, 1859, 938, 4306, 4015, 3228, 2804, 4085, 1890, 3685, 3823, 722, 3719, 3126, 825, 2298, 2592, 1649, 2687, 688, 1409, 2580, 1048, 1502, 4588, 2358, 1587, 872, 2896, 4329, 2180, 2385, 3741, 2172, 2334, 1550, 2118, 881, 2374, 2417, 2148, 4646, 3043, 2004, 3634, 822, 4167, 4120, 2561, 2454, 4450, 2891, 1101, 2214, 4113, 3709, 869, 3225, 1030, 2507, 1999, 1089, 1016, 2744, 2612, 689, 3440, 2914, 3316, 1800, 2245, 4308, 1485, 1161, 1496, 2403, 2068, 3478, 4445, 1031, 4310, 2723, 3536, 2178, 1709, 3899, 2405, 3677, 2629, 4543, 2368, 3339, 3464, 654, 3896, 614, 1299, 2757, 3379, 2978, 1307, 1073, 4548, 2831, 675, 2408, 851, 3366, 741, 3731, 2233, 568, 4290, 1781, 4405, 3164, 4618, 3216, 2674, 4424, 2398, 1742, 2761, 3205, 648, 2042, 3202, 4533, 775, 1054, 2935, 4192, 3072, 811, 3879, 3853, 2098, 3697, 3804, 1439, 3392, 3335, 4522, 4341, 4673, 4344, 2397, 1624, 3841, 4564, 1699, 3118, 2583, 2828, 2622, 4148, 3253, 2171, 645, 1255, 1756, 1207, 4556, 3488, 3087, 794, 2391, 4110, 4459, 708, 3592, 2209, 2115, 1569, 1847, 751, 2087, 820, 1304, 3137, 2040, 2961, 3924, 3796, 4206, 1885, 1292, 1074, 1213, 966, 3263, 1643, 4488, 2018, 3727, 3057, 1001, 2809, 2030, 1655, 3080, 516, 2333, 3675, 1155, 2836, 2982, 3959, 2596, 2915, 1513, 1875, 3882, 3209, 1080, 3975, 3734, 3021, 1026, 1997, 3444, 1561, 819, 3855, 4175, 551, 2702, 678, 3999, 1980, 3791, 717, 1362, 2335, 2278, 1375, 3909, 4293, 2557, 3633, 3224, 3906, 3011, 1506, 3336, 1258, 2802, 2399, 3079, 2686, 3577, 1826, 4271, 4086, 1942, 3463, 4595, 3367, 3076, 3370, 3920, 1043, 4672, 2861, 2673, 2617, 3236, 2711, 2625, 3112, 3259, 1154, 920, 1435, 2246, 3805, 958, 3449, 3471, 2872, 2361, 4525, 1793, 1345, 4644, 1604, 2146, 1959, 2781, 1779, 4530, 3978, 3172, 3417, 4028, 2007, 855, 4248, 3275, 997, 909, 3416, 3195, 3559, 1669, 2902, 3958, 1627, 2439, 4071, 3213, 583, 4507, 796, 3010, 3701, 2535, 3481, 3465, 2482, 605, 4651, 3521, 3503, 3858, 1517, 4432, 3913, 1403, 2731, 669, 1391, 4257, 4560, 3174, 936, 2139, 1128, 3979, 1630, 1705, 1943, 525, 2549, 1547, 624, 1459, 4544, 731, 2788, 3751, 2904, 4305, 3380, 3317, 1268, 2160, 3120, 1241, 4166, 2717, 837, 4294, 3666, 1832, 1906, 2572, 2006, 4514, 3777, 691, 4470, 3624, 3404, 4590, 2300, 603, 1881, 1349, 1186, 4213, 2362, 2522, 4001, 3268, 1592, 2052, 3127, 3139, 1013, 2846, 2608, 2996, 3968, 4461, 3222, 1082, 4657, 1590, 3687, 4436, 512, 2845, 643, 3597, 4641, 1205, 1289, 3337, 3622, 3477, 2646, 1192, 663, 2560, 3156, 3703, 2420, 627, 2061, 1017, 1730, 740, 2425, 759, 860, 4283, 4327, 4298, 1647, 3951, 2355, 2689, 2293, 4303, 3768, 1494, 878, 766, 4513, 3456, 1865, 3238, 3747, 3907, 3386, 1000, 2698, 3344, 4021, 1558, 984, 4126, 3373, 1805, 2201, 2037, 3555, 905, 3035, 588, 672, 4287, 944, 4286, 4080, 4474, 3721, 3355, 3790, 3693, 2122, 4422, 505, 4147, 4479, 1263, 2908, 4366, 2129, 3430, 4501, 3420, 680, 3484, 1848, 4627, 1689, 1267, 1786, 2743, 4426, 2593, 1887, 2732, 1862, 719, 4505, 1813, 1350, 4032, 3008, 866, 4020, 3280, 3291, 4029, 2898, 2501, 2752, 4224, 4027, 4238, 3528, 1799, 3129, 3019, 4589, 3566, 584, 2435, 2056, 1872, 942, 2062, 2749, 895, 953, 3514, 4077, 1769, 2735, 1818, 1331, 3097, 4324, 801, 1845, 3183, 3908, 2162, 3556, 2844, 2265, 2857, 4528, 3070, 4154, 2740, 2392, 3248, 2109, 2747, 3207, 1476, 1631, 3169, 3067, 3767, 906, 3662, 941, 1107, 4661, 4038, 4221, 2014, 948, 1923, 1516, 3167, 3442, 2025, 4431, 3809, 3945, 2264, 4165, 2394, 4066, 931, 1343, 4413, 2443, 3498, 1638, 4289, 3845, 2912, 558, 3331, 1279, 854, 3617, 3017, 2390, 1530, 3450, 3406, 594, 3707, 632, 1708, 1028, 2620, 2541, 3642, 3346, 2797, 760, 4610, 542, 805, 1085, 1230, 757, 4532, 1880, 3393, 853, 3397, 1428, 3307, 4669, 2833, 2275, 2480, 4508, 3651, 3732, 4621, 667, 933, 2793, 1651, 4364, 3639, 1232, 3340, 3745, 3550, 1493, 758, 1179, 1976, 4520, 2279, 1273, 3281, 1294, 3584, 3713, 1666, 4663, 2476, 4408, 4597, 4065, 2570, 818, 3361, 2206, 1927, 1021, 506, 780, 1930, 830, 1319, 2478, 2829, 4061, 3399, 1734, 711, 3029, 1445, 839, 2847, 3891, 1012, 1238, 707, 1144, 3375, 3278, 1025, 4526, 836, 709, 4362, 3059, 2745, 2940, 2924, 1833, 4232, 4547, 828, 1573, 1953, 1614, 2309, 2367, 4620, 1870, 812, 2150, 1570, 2436, 3560, 1884, 1253, 1713, 2552, 1081, 1483, 1619, 3983, 3758, 4411, 4254, 4396, 3575, 4586, 2859, 2610, 1464, 1411, 2317, 1931, 1736, 2074, 2821, 4309, 2414, 804, 2386, 502, 840, 3068, 3557, 4686, 585, 2627, 1090, 3866, 4266, 816, 1254, 951, 3241, 4587, 2884, 3407, 2825, 3508, 1806, 1732, 1574, 4057, 706, 2383, 2132, 2503, 2756, 3673, 877, 3794, 2888, 1733, 3353, 4142, 1200, 3610, 3319, 2874, 2479, 2832, 1637, 4011, 4356, 517, 3613, 4169, 1020, 1528, 2883, 4042, 635, 1252, 3246, 2117, 3854, 2500, 814, 3883, 1083, 3320, 4055, 4438, 2979, 4611, 3414, 1596, 4649, 4026, 1995, 3868, 2636, 2260, 1823, 1581, 3014, 2432, 4152, 1118, 587, 679, 2261, 4176, 2544, 3529, 791, 843, 1568, 2728, 3159, 1559, 4512, 1140, 609, 1229, 4083, 1950, 3871, 3681, 1576, 2063, 4223, 2965, 1189, 1419, 2964, 4687, 3155, 2302, 913, 1984, 3208, 1897, 1432, 3590, 2428, 1499, 4591, 2444, 3058, 3900, 969, 1792, 2426, 1538, 2742, 617, 2623, 2071, 3211, 3729, 596, 606, 2918, 3447, 4336, 3385, 639, 4579, 871, 4392, 4177, 3395, 4373, 3568, 4385, 1315, 4170, 636, 2200, 3987, 3532, 4049, 3310, 3264, 4245, 3848, 4375, 2451, 2437, 1594, 2856, 2619, 3625, 1537, 1657, 2433, 2255, 1964, 2889, 1042, 3210, 1430, 2680, 1949, 3942, 3870, 976, 3083, 2001, 3977, 3132, 3905, 1250, 2603, 3006, 1904, 2318, 2865, 543, 961, 2041, 4010, 2013, 3760, 1149, 3227, 2257, 1972, 2248, 3091, 2614, 1661, 2446, 1209, 1094, 858, 1228, 4137, 2364, 2463, 1836, 1908, 2694, 1318, 2168, 1086, 887, 3049, 3925, 1216, 1450, 2370, 4158, 768, 2324, 901, 3939, 2787, 4078, 1938, 1672, 4390, 1040, 3282, 681, 2438, 1554, 3062, 3517, 4626, 891, 4600, 3627, 3147, 4659, 2352, 2035, 2567, 2932, 3327, 2342, 3003, 2083, 3199, 1788, 4369, 2326, 2542, 3869, 2562, 2830, 4674, 1002, 2125, 3619, 3483, 1245, 1690, 1900, 1492, 2183, 4096, 2149, 2008, 1549, 1608, 2236, 2229, 1512, 3031, 3426, 3368, 4596, 2186, 4412, 510, 1487, 4584, 2471, 1399, 3656, 807, 3614, 3149, 2161, 3260, 1348, 1313, 2887, 974, 564, 623, 730, 3128, 2239, 3328, 3088, 4575, 2656, 2472, 863, 2158, 3206, 2986, 1429, 1992, 1979, 2164, 1087, 4535, 2484, 1314, 1227, 934, 3288, 4539, 3445, 3192, 1951, 1857, 4529, 2076, 3193, 883, 1527, 716, 3901, 2860, 1717, 3730, 1208, 2005, 3970, 2937, 2053, 3851, 2143, 3338, 3897, 1210, 2254, 1567, 2658, 1837, 1827, 1372, 4272, 3060, 2343, 4261, 1752, 2591, 2690, 4331, 1224, 4475, 1688, 2633, 4179, 1825, 2582, 2921, 1129, 3621, 802, 3775, 4440, 3046, 2532, 2027, 2772, 2587, 4609, 3409, 1401, 1850, 1941, 3974, 3436, 4612, 4359, 3960, 2285, 2800, 963, 3989, 1136, 659, 3325, 3429, 1566, 4208, 3302, 2219, 501, 4138, 4455, 2998, 2288, 3273, 2981, 2029, 2486, 2080, 2679, 2488, 1003, 3762, 4253, 880, 3766, 3582, 3138, 4255, 983, 1914, 2240, 1989, 1156, 1084, 3400, 1024, 835, 1500, 923, 3530, 1975, 3538, 2028, 1098, 2730, 2217, 2422, 570, 2465, 1076, 1178, 2594, 2632, 1520, 3161, 1259, 687, 579, 1983, 1588, 1353, 1176, 2774, 3787, 4313, 935, 904, 1829, 3511, 1591, 3196, 3807, 3265, 2431, 4504, 1302, 621, 4183, 3356, 4477, 1332, 2835, 2078, 3716, 3104, 1165, 2777, 1771, 2778, 3276, 3326, 3549, 2360, 649, 4160, 1966, 1839, 4168, 2203, 3028, 896, 2994, 3698, 3304, 2492, 4576, 2138, 1237, 1242, 4403, 3453, 1305, 1243, 4315, 847, 1226, 3491, 3587, 4144, 3542, 800, 3658, 3935, 4640, 3176, 3296, 1998, 2147, 3261, 2337, 3168, 2292, 1711, 3992, 1991, 1456, 1150, 3369, 4415, 1276, 2682, 2816, 3718, 1093, 2483, 3401, 2165, 1584, 1719, 728, 2197, 915, 2085, 4645, 1646, 3839, 1889, 2780, 2303, 2212, 929, 1368, 4460, 3802, 612, 3863, 668, 1004, 2531, 1177, 1270, 1091, 1882, 4613, 1117, 3163, 553, 2775, 1653, 1135, 2806, 4259, 3084, 2842, 946, 2586, 2274, 3641, 2866, 559, 1939, 2226, 2906, 3602, 653, 957, 2419, 4549, 3880, 4104, 2973, 4143, 4047, 4092, 4628, 3133, 3571, 1194, 2140, 4607, 3314, 817, 3847, 4159, 1162, 925, 3446, 4378, 2216, 3776, 2310, 2540, 1524, 3723, 4012, 4457, 4157, 4427, 3250, 4571, 4593, 4099, 4174, 1482, 2901, 2487, 1954, 4363, 3646, 1197, 1137, 4013, 3746, 2116, 4124, 2064, 3887, 1181, 2262, 1741, 4346, 2533, 2773, 1019, 3976, 1522, 4449, 3771, 3284, 3712, 2320, 3106, 4349, 4492, 2215, 1287, 4483, 1188, 3561, 4050, 2088, 3780, 3434, 4139, 4401, 1680, 3676, 1856, 2410, 2277, 3546, 1977, 3115, 2124, 2297, 3885, 2205, 772, 2959, 2344, 3927, 4225, 3219, 4599, 4101, 2110, 1804, 2242, 1863, 1807, 4205, 3842, 3107, 4537, 1271, 1446, 641, 576, 4419, 528, 900, 3950, 742, 4017, 1632, 1442, 1282, 1369, 3315, 1918, 3954, 3789, 4319, 998, 554, 3629, 3177, 3798, 2133, 3243, 4464, 4496, 1784, 3904, 2546, 3423, 4486, 2048, 1366, 1693, 2387, 604, 557, 4391, 3644, 3965, 4388, 2941, 2272, 4536, 3581, 1541, 3898, 4386, 4565, 2624, 868, 1940, 2195, 3952, 1639, 4242, 1145, 1124, 704, 4493, 2563, 1873, 4188, 2455, 4637, 2365, 1597, 2733, 2585, 3513, 3293, 4172, 2176, 2931, 870, 1376, 4105, 4075, 2055, 994, 754, 1755, 1125, 4643, 4563, 1196, 3297, 2597, 3357, 1851, 2708, 764, 4559, 986, 950, 3743, 1342, 2152, 2166, 3523, 4680, 2462, 3457, 1484, 4056, 2284, 4076, 3000, 4088, 4074, 952, 2418, 4090, 4256, 2955, 2434, 2721, 3647, 2962, 4252, 1838, 577, 2347, 3461, 1291, 1109, 4316, 4132, 2267, 2202, 3100, 3626, 2189, 4291, 1898, 4098, 2107, 3074, 2976, 3944, 4342, 3630, 1095, 4043, 1049, 4345, 874, 1055, 3710, 4371, 852, 2553, 1167, 2396, 1595, 2714, 3706, 2251, 1589, 3828, 3638, 748, 2762, 1660, 3664, 3669, 914, 3462, 3499, 4025, 1633, 3742, 4215, 4339, 1072, 732, 3299, 3986, 1557, 3187, 864, 2547, 1893, 4355, 3547, 4397, 3334, 1540, 2514, 2321, 2019, 2485, 1407, 1795, 3506, 3239, 4453, 2060, 3611, 4343, 2864, 3102, 1911, 799, 3034, 1978, 2824, 1239, 1256, 2357, 3822, 959, 3784, 3402, 785, 2605, 1363, 4402, 702, 1123, 2977, 1746, 2850, 2991, 1674, 3947, 3541, 3475, 2313, 4542, 3153, 3516, 1489, 3237, 1843, 1796, 4048, 2534, 1131, 2131, 3408, 1060, 3852, 4446, 3220, 3184, 1067, 2100, 4567, 2393, 1032, 2067, 911, 3233, 3441, 2509, 699, 1716, 4354, 4134, 3093, 1852, 2877, 2520, 1858, 2173, 3661, 4164, 778]
print(type(a[1]))
i=1
y = 0
        
for z in range(len(a)):
    for x in range(len(a)-1):    
        if a[y]<a[i]:
            (a[y],a[i])=(a[i],a[y])
            i+=1
        else:
            i+=1
    i=0
    y+=1
print(a)