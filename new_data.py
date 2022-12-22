all_cids = [135,
174,
177,
180,
222,
240,
241,
243,
289,
299,
356,
359,
379,
402,
403,
527,
544,
700,
702,
712,
713,
727,
785,
798,
807,
887,
931,
932,
943,
948,
980,
985,
991,
992,
995,
996,
1046,
1057,
1119,
1133,
1140,
1480,
1482,
1483,
1486,
1489,
1493,
1615,
1639,
1674,
1732,
1752,
1923,
1982,
1983,
1988,
2078,
2145,
2151,
2153,
2187,
2256,
2266,
2268,
2286,
2314,
2328,
2336,
2337,
2347,
2361,
2450,
2478,
2482,
2519,
2566,
2723,
2728,
2730,
2771,
2812,
2879,
2907,
2912,
2943,
2950,
2969,
3017,
3023,
3026,
3030,
3035,
3036,
3037,
3039,
3048,
3082,
3102,
3117,
3120,
3121,
3198,
3213,
3220,
3224,
3283,
3286,
3293,
3346,
3347,
3352,
3386,
3397,
3473,
3485,
3496,
3518,
3589,
3598,
3610,
3672,
3712,
3715,
3758,
3763,
3767,
3840,
3902,
4004,
4096,
4115,
4130,
4133,
4169,
4189,
4211,
4277,
4534,
4632,
4684,
4696,
4757,
4763,
4764,
4766,
4767,
4788,
4793,
4929,
4933,
4937,
4944,
5035,
5053,
5054,
5100,
5125,
5196,
5212,
5216,
5235,
5327,
5340,
5355,
5455,
5564,
5569,
5727,
5743,
5770,
5794,
5801,
5803,
5833,
5853,
5889,
5943,
5954,
5988,
5991,
5993,
5995,
6001,
6010,
6115,
6129,
6167,
6184,
6197,
6212,
6228,
6253,
6271,
6279,
6293,
6294,
6319,
6323,
6336,
6338,
6344,
6348,
6354,
6358,
6359,
6378,
6421,
6505,
6507,
6529,
6540,
6557,
6569,
6575,
6579,
6580,
6597,
6618,
6619,
6623,
6626,
6643,
6658,
6669,
6697,
6720,
6776,
6777,
6778,
6781,
6782,
6786,
6787,
6795,
6815,
6819,
6853,
6860,
6899,
6914,
6923,
6930,
6931,
6943,
6950,
6982,
6984,
6989,
7003,
7005,
7017,
7047,
7056,
7059,
7074,
7095,
7103,
7112,
7153,
7158,
7175,
7180,
7184,
7204,
7206,
7207,
7224,
7237,
7239,
7245,
7257,
7258,
7261,
7270,
7271,
7276,
7280,
7285,
7290,
7294,
7308,
7311,
7328,
7381,
7391,
7393,
7403,
7406,
7416,
7442,
7452,
7453,
7456,
7469,
7473,
7475,
7478,
7489,
7500,
7501,
7503,
7547,
7563,
7577,
7579,
7618,
7628,
7637,
7638,
7641,
7694,
7705,
7720,
7735,
7767,
7784,
7808,
7809,
7812,
7814,
7833,
7834,
7835,
7839,
7840,
7845,
7855,
7858,
7859,
7900,
7904,
7929,
7933,
7955,
7967,
7971,
8019,
8021,
8028,
8035,
8058,
8076,
8095,
8113,
8117,
8133,
8134,
8141,
8172,
8227,
8252,
8259,
8268,
8289,
8295,
8305,
8342,
8343,
8344,
8361,
8362,
8363,
8364,
8365,
8370,
8371,
8376,
8405,
8411,
8418,
8427,
8434,
8445,
8449,
8456,
8461,
8512,
8554,
8559,
8560,
8561,
8569,
8570,
8571,
8572,
8575,
8606,
8663,
8690,
8697,
8722,
8814,
8831,
8844,
8900,
9106,
9108,
9126,
9128,
9131,
9136,
9137,
9142,
9152,
9153,
9154,
9158,
9161,
9162,
9164,
9171,
9176,
9180,
9181,
9183,
9189,
9198,
9203,
9210,
9215,
9298,
9317,
9322,
9395,
9411,
9502,
9554,
9555,
9777,
9880,
9958,
10208,
10222,
10251,
10436,
10491,
10521,
10522,
10618,
10631,
10680,
10742,
10747,
10787,
10800,
10913,
10943,
10986,
11164,
11169,
11192,
11273,
11313,
11334,
11342,
11374,
11381,
11397,
11442,
11450,
11473,
11742,
11790,
11796,
11816,
11827,
11843,
11852,
11855,
12005,
12101,
12111,
12251,
12433,
12540,
12580,
12688,
12898,
12902,
12968,
13089,
13254,
13263,
13387,
13450,
13618,
13636,
13700,
13708,
13769,
13791,
13869,
13878,
13940,
14052,
14085,
14138,
14145,
14327,
14346,
14347,
14410,
14825,
14851,
14855,
14888,
14905,
14906,
14985,
15032,
15096,
15118,
15202,
15331,
15413,
15415,
15420,
15530,
15531,
15625,
15730,
15731,
15757,
15769,
15787,
15788,
15805,
15910,
15938,
15939,
15965,
16002,
16034,
16043,
16115,
16248,
16305,
16311,
16312,
16318,
16323,
16402,
16421,
16422,
16553,
16653,
16692,
16784,
16932,
16945,
17097,
17132,
17204,
17348,
17412,
17432,
17435,
17481,
17522,
17533,
17570,
18529,
18611,
18617,
18728,
18831,
19427,
19539,
19943,
19988,
20161,
20240,
20392,
20393,
20774,
20965,
21013,
21387,
21419,
21480,
21510,
21648,
21803,
21804,
21805,
22094,
22206,
22544,
22563,
22571,
23017,
23266,
23284,
23448,
23930,
23938,
23973,
23976,
23989,
24085,
24216,
24586,
24639,
24667,
24748,
24870,
24947,
25015,
25059,
25154,
25287,
25429,
25517,
25552,
25622,
25641,
25669,
25670,
25890,
25891,
25893,
26042,
26124,
26176,
26177,
26229,
26295,
26975,
27021,
27144,
27375,
27582,
27668,
27924,
28061,
28115,
28598,
28780,
28936,
29131,
29307,
29352,
29353,
29354,
29393,
29732,
30479,
30541,
30692,
30709,
30773,
30814,
31200,
31233,
31242,
31356,
31357,
31369,
31373,
31404,
31423,
31645,
31677,
31736,
32014,
32154,
32230,
32490,
32781,
32872,
33263,
33473,
33599,
33741,
33743,
34192,
34254,
34277,
34454,
34466,
34469,
34526,
35454,
35781,
35823,
36159,
36186,
36187,
36188,
36231,
36242,
36250,
36324,
36342,
36400,
36401,
36402,
36614,
36647,
36678,
36679,
36870,
36980,
36981,
36982,
37034,
37035,
37036,
37037,
37123,
37175,
37247,
37248,
37249,
37419,
37517,
37542,
37563,
37766,
37803,
37807,
37880,
38012,
38015,
38016,
38017,
38018,
38019,
38024,
38030,
38033,
38037,
38038,
38213,
38251,
38253,
38254,
38284,
38439,
38479,
38779,
38875,
38876,
38884,
39040,
39230,
39327,
39385,
39676,
39681,
39728,
39729,
39800,
39929,
39985,
40024,
40326,
40463,
40467,
40468,
40470,
40471,
40475,
40476,
40585,
40813,
41322,
41368,
41463,
41478,
41539,
41540,
41541,
42027,
42028,
42128,
42129,
42131,
42134,
42138,
42140,
42272,
42836,
42839,
42840,
42844,
42851,
42948,
43226,
43234,
43255,
43495,
43815,
44101,
44284,
44285,
45472,
47167,
47299,
47300,
47650,
47782,
47898,
47936,
49923,
49931,
49973,
50516,
50610,
50897,
50980,
51040,
51041,
51043,
51126,
51130,
51439,
51462,
51464,
51605,
53036,
53154,
53232,
53309,
53524,
54454,
55103,
55104,
55111,
55112,
55119,
55125,
55130,
55133,
55245,
57363,
58167,
59693,
60027,
60059,
60312,
61247,
61529,
61585,
61640,
61899,
62010,
62097,
62329,
62332,
62530,
62753,
63079,
63089,
63090,
63091,
63097,
63103,
63107,
65434,
66030,
66166,
66238,
66461,
66494,
66495,
66532,
66587,
66603,
67114,
67174,
67215,
67296,
67459,
67472,
67473,
67542,
67545,
67733,
67734,
67815,
67818,
67820,
67821,
67822,
68617,
69149,
69150,
69371,
69537,
69619,
69785,
70038,
70355,
70820,
70837,
71245,
72279,
72281,
73665,
73670,
73675,
73852,
73864,
74457,
74483,
74843,
74883,
75371,
75454,
75547,
75607,
75767,
75921,
76302,
76348,
76379,
76739,
76767,
77222,
78111,
78993,
78994,
79234,
79633,
79688,
79717,
80152,
80630,
80715,
80801,
81009,
81259,
82315,
83050,
83494,
83975,
84677,
84691,
86102,
86132,
86138,
86173,
86281,
86291,
86300,
86367,
86393,
86398,
86418,
86429,
87250,
89040,
89440,
89594,
90479,
90571,
91469,
91497,
91552,
91589,
91590,
91631,
91632,
91642,
91644,
91650,
91652,
91653,
91656,
91662,
91664,
91683,
91686,
91687,
91688,
91689,
91692,
91693,
91696,
91699,
91716,
91724,
91727,
91741,
91742,
91753,
91776,
92256,
92292,
92346,
92347,
92383,
92387,
93547,
95170,
96294,
97032,
97039,
97701,
99016,
102614,
102724,
104741,
104853,
104926,
104942,
105036,
105075,
105101,
107377,
107664,
107693,
107698,
107818,
107862,
107904,
107953,
108003,
108023,
108070,
108120,
108132,
108145,
108146,
108178,
108210,
109265,
110635,
111326,
114716,
114733,
114829,
114896,
114900,
114908,
114990,
115209,
115218,
115224,
115240,
117291,
117666,
118216,
119106,
119115,
119141,
119346,
119354,
119359,
119363,
119383,
119518,
119546,
119587,
119704,
122825,
123212,
123351,
123504,
124052,
125430,
128938,
130490,
130780,
135956,
146570,
146640,
149104,
153909,
153962,
153963,
154083,
155094,
155166,
156224,
156484,
157586,
158076,
158264,
158403,
158414,
158629,
162461,
162807,
164567,
164754,
165506,
171852,
176111,
176661,
176890,
177033,
177368,
177870,
177901,
177911,
177947,
178004,
178005,
178006,
178007,
181441,
181731,
181883,
183016,
183439,
183679,
184065,
184066,
184815,
184909,
184910,
184911,
184913,
184914,
186907,
190483,
213013,
213021,
213031,
219592,
220773,
222284,
222757,
228987,
232446,
246598,
249266,
253881,
269933,
296646,
305767,
409301,
439246,
439533,
441404,
442530,
442731,
442793,
443036,
443409,
445154,
445434,
445639,
445858,
447466,
448537,
449459,
456201,
459767,
469625,
480764,
483586,
500199,
513197,
516900,
519286,
526436,
526437,
586708,
590836,
591200,
601234,
608116,
623849,
630355,
637511,
637541,
637760,
637796,
639665,
644178,
644179,
644180,
644181,
644182,
644183,
644209,
656687,
656688,
656692,
657298,
667484,
688628,
697993,
707035,
853433,
919792,
969491,
1549789,
1550472,
1794427,
2288503,
2723650,
2723790,
2733525,
2733526,
2734580,
2776282,
2999413,
3016578,
3018355,
3022255,
3032581,
3032604,
3032732,
3032791,
3032832,
3033832,
3034368,
3035829,
3050412,
3080712,
3086109,
3292100,
3317081,
3391107,
3453883,
4049156,
4201081,
5280343,
5280373,
5280378,
5280443,
5280445,
5280489,
5280863,
5280961,
5281004,
5281377,
5281576,
5281607,
5281654,
5281672,
5281707,
5281708,
5281792,
5281873,
5282240,
5282361,
5282362,
5282363,
5282958,
5284373,
5284378,
5284448,
5284469,
5284484,
5284537,
5284583,
5284596,
5284645,
5288826,
5317742,
5317750,
5324346,
5352425,
5353758,
5354198,
5355130,
5355863,
5357402,
5359485,
5359596,
5359810,
5360515,
5366415,
5366546,
5371562,
5372477,
5377791,
5381226,
5462310,
5462311,
5821911,
5889665,
5941340,
6023583,
6095481,
6327054,
6327815,
6433227,
6434217,
6434236,
6437352,
6437380,
6440554,
6440557,
6442842,
6451142,
6452830,
6850715,
6857447,
9568614,
9570071,
9579578,
9595287,
9817329,
9949848,
9966640,
10017512,
10143739,
10313134,
10342051,
10908094,
10953367,
10985889,
11028658,
11057755,
11067463,
11140605,
11377211,
11626560,
11763618,
11954025,
11954121,
11954125,
11954126,
11954129,
11954131,
11954132,
11954175,
11954193,
11970143,
11978695,
12073149,
12073151,
12110098,
12110099,
12309460,
12309466,
12310947,
12313421,
12358480,
12961638,
13040187,
13283771,
13643667,
13828344,
14252255,
14452637,
15509892,
15509894,
15509895,
15509897,
15509899,
15559699,
15724678,
15768599,
16129698,
16212144,
16682746,
16682804,
16683004,
16684434,
20161169,
21604828,
21604829,
23249466,
23668193,
23668195,
23668197,
23669238,
23672308,
23690444,
42628600,
44251561,
45356234,
45356241,
53249535,
53879331,
54670067,
54675777,
54675779,
54696004,
71316600,
71362053,
71362095,
71374219,
71464055,
72208326,
85729803,
85785801,
86205215,
86208445,
86208471,
86208519,
86287518,
86287519,
90472028,
102196968,
129904873,
]

all_cas = ['50-32-8',
'50-29-3',
'50-00-0',
'51-28-5',
'51-03-6',
'52-68-6',
'52-51-7',
'53-70-3',
'53-19-0',
'54-11-5',
'55-38-9',
'56-55-3',
'56-49-5',
'56-38-2',
'56-36-0',
'56-35-9',
'56-33-7',
'56-23-5',
'57-97-6',
'57-74-9',
'57-68-1 ',
'57-56-7',
'57-55-6',
'57-50-1',
'57-11-4',
'57-10-3',
'58-89-9',
'58-55-9',
'58-08-2',
'59-50-7',
'59-02-9',
'1406-18-4',
'60-82-2',
'60-57-1',
'60-51-5',
'61-82-5',
'62-73-7',
'62-56-6',
'62-38-4',
'63-25-2',
'64-17-5',
'65-85-0',
'66-81-9',
'66-25-1',
'67-97-0',
'67-66-3',
'67-64-1',
'67-56-1',
'68-12-2',
'68-11-1',
'70-70-2',
'70-30-4',
'71-43-2',
'72-55-9',
'72-54-8',
'72-48-0',
'72-43-5',
'72-20-8',
'74-83-9',
'74-31-7',
'75-56-9',
'75-21-8',
'75-15-0',
'75-12-7',
'75-09-2',
'75-07-0',
'75-01-4',
'76-87-9',
'76-44-8',
'76-03-9',
'77-58-7',
'77-40-7',
'77-09-8',
'78-93-3',
'78-79-5',
'78-51-3',
'78-48-8',
'78-42-2',
'79-98-1',
'79-97-0',
'79-95-8',
'79-94-7',
'79-43-6',
'79-07-2',
'79-01-6',
'80-62-6',
'80-54-6',
'80-46-6',
'80-09-1',
'80-05-7',
'81-92-5',
'81-90-3',
'81-15-2',
'81-14-1',
'81-11-8',
'82-68-8',
'82-05-3',
'84-76-4',
'84-75-3',
'84-74-2',
'84-69-5',
'84-66-2',
'84-62-8',
'84-61-7',
'84-60-6',
'84-47-9',
'85-97-2',
'85-70-1',
'85-68-7',
'85-60-9',
'85-01-8',
'86-79-3',
'86-77-1',
'86-73-7',
'86-50-0',
'87-87-6',
'87-86-5',
'87-66-1',
'87-65-0',
'87-22-9',
'88-85-7',
'88-69-7',
'88-30-2',
'88-29-9',
'88-24-4',
'88-18-6',
'88-06-2',
'88-04-0',
'89-72-5',
'89-68-9',
'90-43-7',
'90-15-3',
'90-13-1',
'91-62-3',
'91-58-7',
'1321-65-9',
'1335-88-2',
'91-53-2',
'91-22-5',
'91-20-3',
'92-88-6',
'92-82-0',
'92-69-3',
'92-52-4',
'92-04-6',
'93-76-5',
'93-72-1',
'93-65-2',
'7085-19-0',
'93-45-8',
'94-82-6',
'94-81-5',
'94-80-4',
'94-75-7',
'94-74-6',
'94-41-7',
'94-26-8',
'94-25-7',
'94-18-8',
'94-13-3',
'94-09-7',
'94-06-4',
'25735-67-5',
'95-95-4',
'95-94-3',
'63697-22-3',
'95-80-7',
'95-77-2',
'95-76-1',
'95-57-8',
'95-55-6',
'95-50-1',
'95-20-5',
'96-76-4',
'96-69-5',
'96-45-7',
'96-33-3',
'96-24-2',
'96-18-4',
'96-12-8',
'67708-83-2',
'96-09-3',
'97-77-8',
'97-54-1',
'97-23-4',
'97-17-6',
'98-95-3',
'98-82-8',
'98-73-7',
'98-54-4',
'98-52-2',
'98-29-3',
'99-96-7',
'99-93-4',
'99-76-3',
'99-71-8',
'99-65-0',
'99-53-6',
'100-52-7',
'100-44-7',
'100-42-5',
'100-41-4',
'100-09-4',
'100-02-7',
'100-01-6',
'101-92-8',
'101-80-4',
'101-77-9',
'101-53-1',
'101-21-3',
'101-20-2',
'102-71-6',
'103-23-1',
'103-16-2',
'103-14-0',
'104-76-7',
'104-55-2',
'104-51-8',
'104-43-8',
'104-40-5',
'104-35-8',
'104-13-2',
'105-99-7',
'105-59-9',
'106-99-0',
'106-93-4',
'106-89-8',
'106-88-7',
'106-50-3',
'106-48-9',
'106-47-8',
'106-44-5',
'1319-77-3',
'106-42-3',
'106-41-2',
'107-98-2',
'107-21-1',
'107-19-7',
'107-18-6',
'107-13-1',
'108-95-2',
'108-94-1',
'108-88-3',
'108-78-1',
'108-73-6',
'108-46-3',
'108-43-0',
'108-05-4',
'109-99-9',
'109-89-7',
'109-86-4',
'109-00-2',
'110-80-5',
'110-54-3',
'110-13-4',
'111-84-2',
'111-77-3',
'111-76-2',
'111-65-9',
'111-46-6',
'111-42-2',
'111-30-8',
'111-15-9',
'112-80-1',
'112-34-5',
'112-27-6',
'114-26-1',
'115-96-8',
'115-86-6',
'115-32-2',
'115-29-7',
'115-20-8',
'115-09-3',
'115-07-1',
'116-29-0',
'116-06-3',
'117-99-7',
'117-84-0',
'117-82-8',
'117-81-7',
'117-80-6',
'117-39-5',
'117-10-2',
'118-96-7',
'118-79-6',
'118-75-2',
'118-74-1',
'118-61-6',
'118-60-5',
'118-58-1',
'118-56-9 ',
'118-55-8',
'119-90-4',
'119-65-3',
'119-61-9',
'119-47-1',
'119-36-8',
'119-06-2',
'120-83-2',
'120-80-9',
'120-72-9',
'120-71-8',
'120-58-1',
'120-47-8',
'120-36-5',
'120-21-8',
'120-12-7',
'121-75-5',
'121-14-2',
'122-94-1',
'122-34-9',
'122-14-5',
'123-99-9',
'123-88-6',
'123-73-9',
'123-38-6',
'123-31-9',
'123-30-8',
'123-07-9',
'124-09-4',
'124-07-2',
'126-99-8',
'126-73-8',
'126-00-1',
'127-18-4',
'128-37-0',
'129-73-7',
'129-43-1',
'129-00-0',
'131-70-4',
'131-57-7',
'131-56-6',
'131-55-5',
'131-54-4',
'131-53-3',
'131-18-0',
'131-17-9',
'131-16-8',
'131-11-3',
'132-65-0',
'133-06-2',
'135-19-3',
'136-77-6',
'136-36-7',
'136-23-2',
'137-42-8',
'137-30-4',
'137-26-8',
'139-40-2',
'140-66-9',
'141-43-5',
'141-28-6',
'141-04-8',
'142-82-5',
'142-71-2',
'142-59-6',
'142-47-2',
'143-74-8',
'143-50-0',
'144-55-8',
'147-94-4',
'148-24-3',
'148-18-5',
'149-57-5',
'149-30-4',
'189-64-0',
'189-55-9',
'191-85-5',
'191-30-0',
'192-97-2',
'192-65-4',
'193-39-5',
'195-19-7',
'196-42-9',
'198-55-0',
'205-99-2',
'205-82-3',
'205-25-4',
'206-44-0',
'207-08-9',
'208-96-8',
'213-46-7',
'215-58-7',
'218-01-9',
'224-41-9',
'225-51-4',
'225-11-6',
'226-92-6',
'226-36-8',
'229-87-8',
'230-46-6',
'230-07-9',
'239-35-0',
'239-01-0',
'243-46-9',
'243-17-4',
'253-82-7',
'260-94-6',
'298-00-0',
'299-84-3',
'301-04-2',
'302-04-5',
'307-55-1',
'307-24-4 ',
'309-00-2',
'311-45-5',
'314-40-9',
'319-86-8',
'319-85-7',
'319-84-6',
'327-97-9',
'330-55-2',
'330-54-1',
'333-41-5',
'334-48-5',
'335-76-2',
'335-70-6',
'335-67-1',
'355-46-4',
'355-43-1',
'367-51-1',
'375-95-1',
'375-92-8',
'375-85-9',
'375-80-4',
'375-73-5 ',
'375-50-8',
'375-22-4',
'376-06-7',
'414-29-9',
'446-72-0',
'452-86-8',
'470-90-6',
'472-41-3',
'479-13-0',
'480-41-1',
'480-40-0',
'480-19-3',
'480-18-2',
'481-74-3',
'483-65-8',
'486-66-8',
'487-26-3',
'491-80-5',
'491-70-3',
'500-38-9',
'501-30-4',
'504-15-4',
'507-63-1',
'510-15-6',
'510-13-4',
'518-82-1',
'519-23-3',
'520-36-5',
'520-33-2',
'520-18-3',
'525-82-6',
'530-91-6',
'530-57-4',
'531-95-3',
'533-73-3',
'534-52-1',
'541-73-1',
'541-02-6',
'556-67-2',
'556-52-5',
'557-34-6',
'563-12-2',
'569-64-2',
'10309-95-2',
'2437-29-8',
'573-58-0',
'576-24-9',
'577-33-3',
'578-86-9',
'580-51-8',
'580-16-5',
'582-17-2',
'585-34-2',
'586-96-9',
'593-74-8',
'599-64-4',
'603-45-2',
'604-59-1',
'605-32-3',
'607-12-5',
'608-93-5',
'608-71-9',
'608-25-3',
'611-99-4',
'611-98-3',
'612-83-9',
'615-58-7',
'620-92-8',
'620-17-7',
'625-45-6',
'626-06-2',
'626-03-9',
'631-64-1',
'639-58-7',
'645-56-7',
'647-42-7',
'659-22-3',
'678-41-1',
'678-39-7',
'683-18-1',
'688-73-3',
'709-98-8',
'731-27-1',
'732-26-3',
'754-91-6',
'759-94-4',
'789-02-6',
'831-82-3',
'834-12-8',
'835-11-0',
'843-55-0',
'872-50-4',
'886-50-0',
'892-20-6',
'900-95-8',
'933-75-5',
'935-95-5',
'950-35-6',
'959-98-8',
'992-59-6',
'999-81-5',
'1002-53-5',
'1007-28-9',
'1011-95-6',
'1024-57-3',
'1031-07-8',
'1071-83-6',
'1071-83-6 +',
'1073-67-2',
'1085-98-9',
'1085-12-7',
'1131-60-8',
'1135-24-6',
'1137-59-3',
'1137-42-4',
'1137-41-3',
'1143-72-2',
'1156-51-0',
'1163-19-5',
'1222-05-5',
'1303-96-4',
'1306-25-8',
'1310-65-2',
'1314-13-2',
'1317-35-7',
'1327-53-3',
'1330-43-4',
'1330-20-7',
'1332-82-7',
'7646-79-9',
'1332-40-7',
'1338-24-5',
'1344-09-8',
'1344-08-7',
'1313-82-2',
'1415-93-6',
'1461-25-2',
'1461-23-0',
'1461-22-9',
'1470-94-6',
'1470-79-7',
'1470-57-1',
'1478-61-1',
'1506-02-1',
'21145-77-7',
'1518-83-8',
'1563-66-2',
'1570-64-5',
'1571-75-1',
'1576-13-2',
'1582-09-8',
'1593-77-7',
'1596-84-5',
'1634-78-2',
'1634-04-4',
'1638-22-8',
'1675-54-3',
'1689-84-5',
'1689-83-4',
'1689-82-3',
'1745-89-7',
'1746-01-6',
'1805-61-4',
'1806-29-7',
'1806-26-4',
'1825-31-6',
'1836-77-7',
'1836-75-5',
'1861-32-1',
'1895-26-7',
'1897-45-6',
'1910-42-5',
'1912-24-9',
'1918-02-1',
'1918-00-9',
'1928-37-6',
'1929-73-3',
'1937-37-7',
'1943-97-1',
'1943-79-9',
'1982-47-4',
'1987-50-4',
'2024-88-6',
'2032-65-7',
'2039-87-4',
'2039-85-2',
'2043-47-2',
'2050-75-1',
'2050-74-0',
'2051-62-9',
'2051-60-7',
'2051-24-3',
'2057-49-0',
'2058-94-8',
'2081-08-5',
'2104-96-3',
'2104-64-5',
'2167-51-3',
'2212-67-1',
'2234-13-1',
'2246-69-7',
'2310-17-0',
'2315-67-5',
'2315-61-9',
'2353-45-9',
'2381-21-7',
'2385-85-5',
'2387-23-7',
'2396-68-1',
'2429-74-5',
'2437-79-8',
'2443-58-5',
'2481-94-9',
'2491-32-9',
'2497-59-8',
'2528-16-7',
'2580-78-1',
'2581-34-2',
'2589-73-3',
'2593-15-9',
'2597-11-7',
'2597-03-7',
'2619-00-3',
'91384-85-9',
'2636-26-2',
'2642-82-2',
'2657-25-2',
'2664-63-3',
'2682-20-4',
'2706-90-3',
'2764-72-9',
'2783-94-0',
'2795-39-3',
'2921-88-2',
'2971-36-0',
'3001-15-8',
'3010-80-8',
'3050-88-2',
'3115-49-9',
'3194-55-6',
'25637-99-4',
'3234-61-5',
'3252-43-5',
'3253-39-2',
'3282-56-2',
'3319-31-1',
'3322-93-8',
'3380-34-5',
'3424-82-6',
'3600-64-4',
'3697-24-3',
'3739-38-6',
'3825-26-1',
'3846-71-7',
'3972-65-4',
'4032-26-2',
'4065-45-6',
'4167-74-2',
'4170-30-3',
'4191-73-5',
'4247-02-3',
'4250-77-5',
'4376-20-9',
'4376-18-5',
'4399-55-7',
'4400-06-0',
'4685-14-7',
'4824-78-6',
'4901-51-3',
'5026-12-0',
'5103-74-2',
'5103-73-1',
'5103-71-9',
'5153-25-3',
'5180-04-1',
'14868-03-2',
'5315-79-7',
'5329-12-4',
'5335-24-0',
'5385-75-1',
'5394-98-9',
'5409-83-6',
'5436-43-1',
'5466-77-3',
'5471-51-2',
'5598-52-7',
'5598-15-2',
'5598-13-0',
'5613-46-7',
'5836-10-2',
'5915-41-3',
'5975-78-0',
'6027-13-0',
'6051-87-2',
'6052-84-2',
'6073-11-6',
'6164-98-3',
'6190-65-4',
'6197-30-4',
'6335-83-7',
'6362-80-7',
'6386-73-8',
'6465-74-3',
'6465-71-0',
'6473-13-8',
'6484-52-2',
'6515-38-4',
'6515-37-3',
'6521-30-8',
'6640-27-3',
'6665-83-4',
'6754-58-1',
'6807-17-6',
'6846-50-0',
'6863-24-7',
'6923-22-4',
'6949-73-1',
'7012-37-5',
'7099-43-6',
'7173-51-5',
'7235-40-7',
'7287-19-6',
'7311-27-5',
'7425-79-8',
'7429-90-5',
'7439-97-6',
'7439-96-5',
'7439-92-1',
'7439-89-6',
'7440-66-6',
'7440-47-3',
'7440-43-9',
'7440-39-3',
'7440-38-2',
'7440-22-4',
'7446-09-5',
'7446-08-4',
'7447-41-8',
'7447-40-7',
'7447-39-4',
'7487-94-7',
'7601-89-0',
'14797-73-0',
'7631-99-4',
'7631-95-0',
'7632-00-0',
'7646-85-7',
'7647-15-6',
'7651-83-4',
'7664-41-7',
'7681-49-4',
'7696-12-0',
'7705-07-9',
'7718-54-9',
'7733-02-0',
'7758-98-7',
'7758-19-2',
'7761-88-8',
'7772-99-8',
'7773-01-5',
'7778-74-7',
'14797-73-0',
'7783-20-2',
'7783-06-4',
'7784-46-5',
'7786-81-4',
'7786-80-3',
'113-48-4',
'7786-34-7',
'7786-30-3',
'7789-38-0',
'7789-00-6',
'7790-98-9',
'14797-73-0',
'8001-35-2',
'8002-05-9',
'8003-34-7',
'8008-20-6',
'8016-25-9 ',
'8018-01-7',
'8068-44-8',
'9000-11-7',
'9002-93-1',
'9004-62-0',
'9005-65-6',
'9006-42-2',
'9016-45-9',
'9036-19-5',
'9036-19-5',
'68412-54-4',
'10024-97-2',
'10025-91-9',
'10041-02-8',
'10043-35-3',
'10045-97-3',
'10049-05-5',
'10049-04-4',
'10099-74-8',
'10102-18-8',
'10108-64-2',
'10222-01-2',
'10265-92-6',
'10361-37-2',
'10380-28-6',
'10448-09-6',
'10453-86-8',
'10527-11-4',
'10605-21-7',
'11066-49-2',
'11096-82-5',
'11097-69-1',
'11104-28-2',
'12108-13-3',
'12122-67-7',
'12125-02-9',
'12238-49-2',
'12427-38-2',
'12616-36-3',
'12616-35-2',
'12642-23-8',
'12672-29-6',
'13020-57-0',
'13029-08-8',
'13037-86-0',
'13049-13-3',
'13067-93-1',
'13071-79-9',
'13108-52-6',
'13171-21-6',
'13171-00-1',
'13241-28-6',
'13311-84-7',
'13345-26-1',
'13345-23-8',
'13345-21-6',
'13356-08-6',
'13410-01-0',
'13463-67-7',
'13464-24-9',
'13510-49-1',
'13520-83-7',
'13552-44-8',
'13593-03-8',
'13595-25-0',
'13674-87-8',
'13674-84-5',
'13826-35-2',
'14173-30-9',
'14409-72-4',
'14484-64-1',
'14755-02-3',
'14938-35-3',
'14962-28-8',
'15087-24-8',
'15231-91-1',
'15323-35-0',
'15499-27-1',
'15545-48-9',
'15725-12-9',
'15950-66-0',
'15972-60-8',
'16065-83-1',
'16423-68-0',
'16752-77-5',
'16867-04-2',
'17062-87-2',
'17404-66-9',
'17573-21-6',
'17696-62-7',
'17804-35-2',
'17924-92-4',
'17927-65-0',
'17964-44-2',
'18181-80-1',
'18259-05-7',
'18540-29-9',
'18854-01-8',
'18979-55-0',
'18979-53-8',
'18979-50-5',
'19044-88-3',
'19666-30-9',
'20071-09-4',
'20265-96-7',
'20291-73-0',
'20325-40-0',
'20426-12-4',
'20427-84-3',
'20636-48-0',
'20763-88-6',
'21087-64-9',
'21245-02-3',
'21340-02-3',
'21388-77-2',
'21564-17-0',
'21609-90-5',
'21725-46-2',
'21787-80-4',
'21850-44-2',
'22717-94-8',
'22781-23-3',
'23103-98-2',
'23135-22-0',
'23184-66-9',
'23593-75-1',
'23719-22-4',
'23950-58-5',
'24151-93-7',
'24579-73-5',
'24643-97-8',
'25013-16-5',
'25057-89-0',
'25074-67-3',
'25154-52-3',
'25311-71-1',
'25550-58-7',
'25913-05-7',
'26002-80-2',
'26027-38-3',
'26264-02-8',
'26306-61-6',
'26401-74-1',
'26523-78-4',
'26543-97-5',
'26571-11-9',
'26761-40-0',
'26970-82-1',
'27147-75-7',
'27176-93-8',
'68412-54-4',
'27177-05-5',
'27208-37-3',
'27459-10-5',
'27575-78-6',
'27697-00-3',
'27942-27-4',
'28034-99-3',
'28057-48-9',
'28159-98-0',
'28213-80-1',
'28249-77-6',
'28463-03-8',
'28469-92-3',
'28553-12-0',
'68515-48-0',
'68515-48-0',
'28822-58-4',
'28994-41-4',
'29082-74-4',
'29091-21-2',
'29232-93-7',
'29420-49-3',
'29426-78-6',
'29772-02-9',
'29799-07-3',
'30026-85-8',
'30560-19-1',
'115096-11-2',
'30746-58-8',
'30784-32-8',
'30784-31-7',
'30784-30-6',
'30784-27-1',
'31127-54-5',
'31508-00-6',
'31631-13-7',
'31751-59-4',
'32534-81-9',
'32598-14-4',
'32598-13-3',
'32598-12-2',
'32598-11-1',
'32774-16-6',
'32809-16-8',
'32861-85-1',
'33089-61-1',
'33104-11-9',
'33146-45-1',
'33204-77-2',
'33204-76-1',
'33213-65-9',
'33284-54-7',
'33284-53-6',
'33704-61-9',
'33857-28-2',
'33979-03-2',
'34113-46-7',
'34123-59-6',
'34166-38-6',
'34256-82-1',
'34588-40-4',
'34643-46-4',
'34883-43-7',
'34883-41-5',
'34883-39-1',
'35065-30-6',
'35065-29-3',
'35065-28-2',
'35065-27-1',
'35367-38-5',
'35554-44-0',
'35693-99-3',
'35693-92-6',
'35694-04-3',
'35779-04-5',
'35854-94-5',
'35964-76-2',
'36335-67-8',
'36455-72-8',
'36559-22-5',
'36734-19-7',
'36861-47-9',
'37205-87-1',
'37515-51-8',
'37680-73-2',
'37680-65-2',
'37872-24-5',
'37994-82-4',
'38028-27-2',
'38379-99-6',
'38380-08-4',
'38380-07-3',
'38380-05-1',
'38380-04-0',
'38380-03-9',
'38411-22-2',
'38444-88-1',
'38444-81-4',
'38444-76-7',
'38713-56-3',
'38964-22-6',
'39227-61-7',
'39227-58-2',
'39227-28-6',
'39300-45-3',
'39515-51-0',
'39635-35-3',
'39635-32-0',
'39765-80-5',
'39801-14-4',
'40321-76-4',
'40346-55-2',
'40487-42-1',
'40596-69-8',
'40957-83-3',
'41096-46-2',
'41198-08-7',
'41317-15-1',
'41318-75-6',
'41351-30-8',
'41451-28-9',
'41464-40-8',
'41483-43-6',
'41814-78-2',
'42019-78-3',
'42422-68-4',
'42576-02-3',
'42588-37-4',
'42874-03-3',
'43121-43-3',
'43141-69-1',
'50471-44-8',
'50512-35-1',
'50585-46-1',
'50585-41-6',
'50585-40-5',
'50594-67-7',
'50670-76-3',
'51134-25-9',
'51200-87-4',
'51207-31-9',
'51218-49-6',
'51218-45-2',
'51230-49-0',
'51338-27-3',
'51630-58-1',
'51974-40-4',
'51990-12-6',
'52315-07-8',
'52427-13-1',
'52645-53-1',
'52663-69-1',
'52663-68-0',
'52663-65-7',
'52663-63-5',
'52663-60-2',
'52663-59-9',
'52918-63-5',
'53112-28-0',
'53459-39-5',
'53469-21-9',
'53555-64-9',
'53558-25-1',
'53623-59-9',
'53623-42-0',
'53846-50-7',
'53905-33-2',
'53905-30-9',
'53905-29-6',
'53905-28-5',
'55179-31-2',
'55219-65-3',
'55406-53-6',
'55512-33-9',
'55566-30-8',
'55701-05-8',
'55702-46-0',
'55702-45-9',
'56558-16-8',
'56858-70-9',
'56892-31-0',
'56892-30-9',
'57018-04-9',
'57103-57-8 ',
'67314-98-1',
'61080-23-7',
'see also 66241-09-6',
'57117-44-9',
'57117-41-6',
'57117-37-0',
'57117-34-7',
'57117-32-5',
'57117-31-4',
'57342-02-6',
'57404-88-3',
'57427-55-1',
'57465-28-8',
'57678-03-2',
'58802-20-3',
'58802-16-7',
'58802-15-6',
'58802-08-7',
'58863-14-2',
'59080-40-9',
'59536-65-1',
'59870-68-7',
'60044-26-0',
'60168-88-9',
'60207-90-1',
'60348-60-9',
'60390-27-4',
'60851-34-5',
'60983-69-9',
'61445-50-9',
'63019-39-6',
'63019-38-5',
'63041-56-5',
'63041-53-2',
'63284-71-9',
'63449-39-8',
'63935-38-6',
'63987-19-9',
'64126-87-0',
'64126-86-9',
'64249-01-0',
'64359-81-5',
'64401-02-1',
'64529-56-2',
'64742-95-6',
'64742-88-7',
'64920-31-6',
'65195-55-3',
'65510-44-3',
'65945-06-4',
'65997-15-1',
'66063-05-6',
'66230-04-4',
'66246-88-6',
'66332-96-5',
'66575-29-9',
'66640-61-7',
'66640-60-6',
'66640-58-2',
'67517-48-0',
'67554-50-1',
'67562-40-7',
'67651-37-0',
'67651-36-9',
'67651-34-7',
'67733-57-7',
'67747-09-5',
'67888-99-7',
'67922-26-3',
'68085-85-8',
'68140-48-7',
'68236-13-5',
'68296-97-9',
'68308-87-2',
'68359-37-5',
'68412-54-4',
'68631-49-2',
'68694-11-1',
'68917-43-1',
'69409-94-5',
'69698-57-3',
'69806-50-4',
'70124-77-5',
'70356-09-1',
'70362-50-4',
'70362-47-9',
'70648-26-9',
'70648-21-4',
'70872-29-6',
'71030-11-0',
'71561-11-0',
'71617-10-2',
'71751-41-2',
'71855-45-3',
'71859-30-8',
'71945-81-8',
'71998-74-8',
'71998-72-6',
'72108-22-6',
'72490-01-8',
'79127-80-3',
'72624-02-3',
'72629-94-8',
'72861-06-4',
'73250-68-7',
'73575-54-9',
'74115-24-5',
'74192-35-1',
'74472-44-9',
'74472-37-0',
'74499-35-7',
'74738-17-3',
'74992-96-4',
'75736-33-3',
'75938-34-0',
'76253-60-6',
'111483-93-3',
'76621-12-0',
'76674-21-0',
'76738-62-0',
'77029-19-7',
'77029-18-6',
'77102-82-0',
'79755-43-4',
'79881-33-7',
'79983-71-4',
'80844-07-1',
'82019-04-3',
'82019-03-2',
'82657-04-3',
'82845-25-8',
'83704-53-4',
'83704-50-1',
'83704-45-4',
'83704-39-6',
'83704-32-9',
'83704-31-8',
'83704-30-7',
'83704-22-7',
'83704-21-6',
'83792-61-4',
'84030-79-5',
'84082-61-1',
'84852-15-3',
'85422-92-0',
'85509-19-9',
'85535-85-9',
'86479-06-3',
'87130-20-9',
'88283-41-4',
'88671-89-0',
'88966-74-9',
'88966-73-8',
'88966-71-6',
'88966-70-5',
'88966-69-2',
'88966-68-1',
'90045-36-6',
'90481-04-2',
'91465-08-6',
'93050-79-4',
'93912-64-2',
'93925-00-9',
'94361-06-5',
'95342-41-9',
'95737-68-1',
'96491-05-3',
'97741-80-5',
'100231-56-9',
'100532-36-3',
'100702-98-5',
'101200-48-0',
'102570-52-5',
'103124-63-6',
'103426-97-7',
'103426-96-6',
'103426-95-5',
'103426-94-4',
'103426-92-2',
'104086-18-2',
'105906-36-3',
'106599-06-8',
'107342-55-2',
'107534-96-3',
'107555-93-1',
'109333-35-9',
'109333-34-8',
'109333-33-7',
'109333-32-6',
'109333-31-5',
'109333-30-4',
'109591-02-8',
'110488-70-5',
'110726-28-8',
'110999-44-5',
'111810-41-4',
'111988-49-9',
'112344-57-7',
'114369-43-6',
'115481-73-7',
'116806-76-9',
'116807-53-5',
'116807-52-4',
'117718-60-2',
'118174-38-2',
'119209-27-7',
'119446-68-3',
'120068-37-3',
'121158-58-',
'121552-61-2',
'124495-18-7',
'124882-64-0',
'125652-16-6',
'125652-14-4',
'125652-13-3',
'125652-12-2',
'126833-17-8',
'127087-87-0',
'129880-08-6',
'130689-92-8',
'130892-67-0',
'130892-66-9',
'131167-12-9',
'131341-86-1',
'133855-98-8',
'135319-73-2',
'106325-08-0',
'134237-52-8',
'134237-51-7',
'134237-50-6',
'135410-20-7',
'160430-64-8',
'138261-41-3',
'139883-51-5',
'139883-50-4',
'142459-58-3',
'142648-65-5',
'142731-63-3',
'145413-90-7',
'147217-73-0',
'149111-99-9',
'149589-56-0',
'149790-22-7',
'149949-90-6',
'149949-88-2',
'150224-16-1',
'150304-11-3',
'150304-10-2',
'150304-08-8',
'150975-81-8',
'152969-11-4',
'153719-23-4',
'155999-95-4',
'156609-10-8',
'158076-69-8',
'158076-68-7',
'158076-64-3',
'158076-63-2',
'158076-62-1',
'172485-99-3',
'172485-98-2',
'172485-96-0',
'172486-00-9',
'178928-70-6',
'182346-21-0',
'186825-39-8',
'186825-36-5',
'188425-85-6',
'189084-68-2',
'189084-67-1',
'189084-66-0',
'189084-64-8',
'189084-63-7',
'189084-62-6',
'189084-60-4',
'189084-58-0',
'189084-57-9',
'189578-02-7',
'189578-00-5',
'192190-10-6',
'192190-09-3',
'207122-16-5',
'210555-94-5',
'210880-92-5',
'223749-10-8',
'243982-82-3',
'288864-02-8',
'337513-54-9',
'354529-50-3',
'446254-48-4 ',
'521947-27-3',
'741687-98-9',
'852541-30-1',
'852541-25-4',
'852541-21-0',
'854904-93-1',
'854904-92-0',
'857629-71-1',
'861010-65-3',
'861011-60-1',
'911370-98-4',
'911371-07-8',
'911371-06-7',
'1119449-38-5',
'1119449-37-4',
'1139800-98-8',
'1471311-26-8',
'1782069-81-1',
'1824346-00-0',]

def cas_to_cid():
    import easy_entrez
    from easy_entrez.parsing import xml_to_string
    all_cids = set()

    entrez_api = easy_entrez.EntrezAPI(
        'endoscreen',
        'verditelabs@gmail.com',
        # optional
        return_type='json'
    )
    import time
    for cas in all_cas:
        time.sleep(1)
        chem = entrez_api.search(cas, max_results = 10, database='pccompound')
        cid = chem.data['esearchresult']['idlist']
        #if len(cid) > 1:
        #    print(cid)
        all_cids.update(cid)
        print(cas,cid)
    print(all_cids)
    print(all_cids)

def find_duplicates():
    import pubchempy as pcp
    out_cids = set()
    found_cas = set()
    for cid in all_cids:
        synonyms = pcp.Compound.from_cid(cid).synonyms
        asdf = list(filter(lambda x: x in all_cas, synonyms))
        if len(asdf) > 1:
            # the CID has a CAS match
            out_cids.add(cid)
            found_cas.update(set(asdf))
        else:
            print()

        print(asdf)
    print("all cids", out_cids)
    print("leftover CAS", set(all_cas) - found_cas)

#find_duplicates()
cas_to_cid()