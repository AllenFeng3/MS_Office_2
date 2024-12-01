show databases ;
use toeflcet46;

select word,  'cet46-official' as  'sources' from `0-cet46-official`;  # 7998

select word, 'cet46' as 'sources' from `03-cet46` union
select word, 'cet4' as 'sources' from `99-cet4` union
select word, 'cet6' as 'sources' from `99-cet6` union
select word, 'postgraduate' as 'sources' from `99-others` union
select word, 'postgraduate' as 'sources' from `postgraduatewords` union
select word, 'postgraduate' as 'sources' from `98-kaoyan` union
select word, 'postgraduate' as 'sources' from `highschoolwords` union
select word, 'cet8' as 'sources' from `99-cet8` union
select word, 'gmat' as 'sources' from `99-gmat` union
select word, 'gre' as 'sources' from `99-gre` union
select word, 'sat' as 'sources' from `99-sat` union
select word, 'toefl' as 'sources' from `99-toefl` union
select word, 'ielts' as 'sources' from `99-ielts` union
select word, 'bec' as 'sources' from `99-bec` union
select word, 'senior' as 'sources' from `02-senior-school` union
select word, 'senior' as 'sources' from `98-senior` union
select word, 'junior' as 'sources' from `98-junior` union
select word, 'primary' as 'sources' from `99-primary`;

SELECT *
FROM `97-words`
WHERE word NOT IN (
    SELECT word
    FROM `0-cet46-official`
);