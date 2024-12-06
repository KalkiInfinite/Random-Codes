factor(age, [infant, child, teenager, young_adult, adult, senior]).
factor(gender, [male, female]).
factor(lifestyle_habit, [sedentary, moderately_active, active]).
factor(pre_existing_condition, [diabetes, hypertension, obesity, high_cholesterol, smoking, family_history]).

risk_of_heart_disease(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Age == senior ; Conditions == [diabetes, hypertension, high_cholesterol]),
    Risk is 3;
    Conditions == [hypertension, high_cholesterol],
    Risk is 2;
    Risk is 1.

risk_of_diabetes(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Age == adult, Gender == male, Lifestyle == sedentary, Conditions == []),
    Risk is 2;
    (Age == senior, Conditions == [obesity, family_history]),
    Risk is 3;
    Risk is 1.

risk_of_hypertension(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Age == adult, Conditions == [obesity, family_history]),
    Risk is 2;
    (Age == senior, Gender == female, Conditions == [family_history]),
    Risk is 3;
    Risk is 1.

risk_of_obesity(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Lifestyle == sedentary),
    Risk is 2;
    (Conditions == [diabetes, hypertension]),
    Risk is 3;
    Risk is 1.

risk_of_high_cholesterol(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Age == adult, Gender == male, Lifestyle == sedentary),
    Risk is 2;
    (Age == senior, Conditions == [hypertension]),
    Risk is 3;
    Risk is 1.

risk_of_smoking_related_diseases(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Gender == male, Conditions == [smoking]),
    Risk is 3;
    (Gender == female, Age == adult, Conditions == [smoking]),
    Risk is 2;
    Risk is 1.

risk_of_family_history_related_diseases(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Age == adult, Gender == male, Conditions == [family_history]),
    Risk is 2;
    (Age == senior, Gender == female, Conditions == [family_history]),
    Risk is 3;
    Risk is 1.

risk_of_stress_related_diseases(Age, Gender, Lifestyle, Conditions, Risk) :-
    (Age == adult, Gender == female, Lifestyle == sedentary, Conditions == [stress]),
    Risk is 3;
    (Age == young_adult, Gender == male, Conditions == [stress]),
    Risk is 2;
    Risk is 1.

calculate_overall_risk(Age, Gender, Lifestyle, Conditions, OverallRisk) :-
    risk_of_heart_disease(Age, Gender, Lifestyle, Conditions, Risk1),
    risk_of_diabetes(Age, Gender, Lifestyle, Conditions, Risk2),
    risk_of_hypertension(Age, Gender, Lifestyle, Conditions, Risk3),
    risk_of_obesity(Age, Gender, Lifestyle, Conditions, Risk4),
    risk_of_high_cholesterol(Age, Gender, Lifestyle, Conditions, Risk5),
    risk_of_smoking_related_diseases(Age, Gender, Lifestyle, Conditions, Risk6),
    risk_of_family_history_related_diseases(Age, Gender, Lifestyle, Conditions, Risk7),
    risk_of_stress_related_diseases(Age, Gender, Lifestyle, Conditions, Risk8),
    OverallRisk is (Risk1 + Risk2 + Risk3 + Risk4 + Risk5 + Risk6 + Risk7 + Risk8) / 8.

display_risk_level(Risk) :-
    Risk =< 1.5,
    write('Low risk');
    Risk =< 2.5,
    write('Moderate risk');
    write('High risk').
