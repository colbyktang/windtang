// import * as firebase from 'firebase/app';
// import 'firebase/analytics';
import firebase from 'firebase';
import 'firebase/storage';
import 'firebase/firestore';

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBTeVKPKspieAPPhtRfF9T-Wl8p4Vzsk-o",
    authDomain: "wind-tang.firebaseapp.com",
    projectId: "wind-tang",
    storageBucket: "wind-tang.appspot.com",
    messagingSenderId: "499897299825",
    appId: "1:499897299825:web:38ff9921d683a7c0fb3cd0",
    measurementId: "G-2X3MRMFLYF"
  };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
// firebase.analytics();

const projectStorage = firebase.storage();
const projectFirestore = firebase.firestore();
const timestamp = firebase.firestore.FieldValue.serverTimestamp;

export { projectStorage, projectFirestore, timestamp};