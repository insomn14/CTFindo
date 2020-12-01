echo 'KKSI2020{abcdefghijklmnopqrstu}' > test.txt; wine encryptor.exe encrypt must_be_keys test.txt outfile; xxd -i outfile
