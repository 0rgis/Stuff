

---

## Hashes



```sh
1. $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG
2. 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1
3. $6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0
4. b6b0d451bbf6fed658659a9e7e5598fe
```

**Method**

*all hashes were saved in seperate files, 1.txt,3.txt for hashcat, other 2 copy n paste*

1. [Identified hash with this site](https://www.tunnelsup.com/hash-analyzer/)
	>**Hash type:** bcrypt
	
	Hashcat code for bcrypt is 3200(hashcat -h) & i used rockyou.txt
	
	`hashcat -m 3200 1.txt /usr/share/wordlists/rockyou.txt --force`
	
	![[Pasted image 20210522162738.png]]
	
	
2. [cracked hash here](https://hashes.com/en/decrypt/hash)
	>![[Pasted image 20210522163409.png]]


3. This is Sha512crypt & the code can be found on hashcat site, it's 1800 for this
	*to be updated with the hashidentifier site link n screenshot etc*
	`hashcat -m 1800 3.txt /usr/share/wordlists/rockyou.txt --force`
	
	![[Pasted image 20210522163713.png]]
	
4. [cracked hash here](https://hashes.com/en/decrypt/hash)
	>![[Pasted image 20210522164120.png]]


**Results**

![[Pasted image 20210522160514.png]]




[tips frome this site](https://fthcyber.com/2020/09/28/hashing-crypto-101-writeup-tryhackme/)


*to do*
replace or add text for images as github doesnot show the imgs, add the result in blockcode under image
