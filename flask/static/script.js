const dbConfig = {
    collection: 'raspberry',
    document: 'senne-pi'
};

const firebaseConfig = {
    apiKey: "AIzaSyDIoR432I4FEURkwc6enFDtf_Us4KgA8DE",
    authDomain: "iotlabosenne.firebaseapp.com",
    databaseURL: "https://iotlabosenne.firebaseio.com",
    projectId: "iotlabosenne",
    storageBucket: "iotlabosenne.appspot.com",
    messagingSenderId: "637046717796",
    appId: "1:637046717796:web:3f9b270e524f598857ce71",
    measurementId: "G-SWEGMQHY08"
  };

  const app = {
    init() {
        // initialiseer de firebase app
        firebase.initializeApp(firebaseConfig);
        this._db = firebase.firestore();
        this.cacheDOMElements();
        this.cacheDOMEvents();
        this.readSensorData();

        this._matrix = {
            isOn: false, color: {value: '#000000', type: 'hex'}
        };
    },
    cacheDOMElements() {
        this.$colorPicker = document.querySelector('#colorPicker');
        this.$toggleMatrix = document.querySelector('#toggleMatrix');
        this.$btnChange = document.querySelector('#btnChange');
        this.$temperature = document.getElementById('temperature');
        this.$humidity = document.getElementById('humidity');
    },
    cacheDOMEvents() {
        this.$btnChange.addEventListener('click', (e) => {
            e.preventDefault();
            this._matrix.color.value = this.$colorPicker.value;
            this._matrix.isOn = this.$toggleMatrix.checked;
            
            this.updateInFirebase();
        });
    },
    updateInFirebase() {
        this._db.collection(dbConfig.collection).doc(dbConfig.document)
            .set(
                {matrix: this._matrix},
                {merge: true}
            );
    },
    readSensorData() {
        const temperature = document.getElementById('temperature');
        const humidity = document.getElementById('humidity');

        this._db.collection('raspberry').doc('sensor')
        .onSnapshot((doc) => {
            console.log(doc.data());
            temperature.innerText = `${parseFloat(doc.data().temperature).toFixed(2)} °C`;
            humidity.innerText = `${parseFloat(doc.data().humidity).toFixed(2)} %`;
        })
    }
}

app.init();