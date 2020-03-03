
public class{
	Serializable obj = new String("enigma");
	KeyGenerator kgen = KeyGenerator.getInstance("AES");
	kgen.init(128);
	SecretKey aesKey = kgen.generateKey();
	Cipher cipher = Cipher.getInstance("AES");
	cipher.init(Cipher.ENCRYPT_MODE, aesKey);
	SealedObject sealedObject = new SealedObject[obj, cipher);
	System.out.println("sealedObject-"+ sealedObject);
	System.out.println("sealedObject data-"+ sealedObject.getObject(aesKey));


}
