import QtQuick.Controls 1.4
import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Controls.Material 2.2
import QtGraphicalEffects 1.0
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import "../Common"

Item {
    id: root
    anchors.fill: parent

    property string primaryColor: Material.Red;
    property string secondaryColor: Material.Green;
    property string backgroundColor: Material.color(Material.Grey, Material.Shade50);

    property QtObject testSuite: null;

    property var locale: Qt.locale()

    QtObject {
        id: internal
        property int _curIdx: 0
    }

    onTestSuiteChanged: {
        if (testSuite !== null) {
            testSuite.setStepType("regular");
            testSuite.sequenceComplete.connect(onSequenceComplete)
            testSuite.sequenceStart.connect(onSequenceStart)
            testSuite.stepStart.connect(onStepStart)
            testSuite.stepComplete.connect(onStepComplete)
            testSuite.deviceIDSet.connect(onDeviceID)
        }
    }

    function onStepStart(caseName, idx, numCases) {
        var myIdx = idx+1;
        curResult.text = curResult.text+ "\n" + caseName + "(" + myIdx +" von " + numCases + ")"
    }

    function onStepComplete(state, result, msg, fullName, idx, numCases) {
        curResult.text = curResult.text + "\n" + msg
    }

    function onDeviceID(deviceID) {
        resultDevID.text = deviceID;
    }

    function onSequenceStart () {
        var now  = new Date();

        sucIcon.visible = false;
        errIcon.visible = false;
        busy.visible = true;
        resultCaption.text = qsTr("Busy");
        resultDevID.text = qsTr("Unbekanntes Gerät");
        txtStart.text = qsTr("Start: " + now.toLocaleTimeString(Qt.locale(), "hh:mm:ss"));
        curResult.text = "";
    }

    function onSequenceComplete (suiteState, success, duration, values) {
        txtDuration.text = qsTr("Dauer: " + Number.parseFloat(duration).toFixed(2) + " s")
        if (success)
        {
            playSound.playSuccess()
            sucIcon.visible = true;
            errIcon.visible = false;
            sucIcon.animate()
            busy.visible = false;
            resultCaption.text = qsTr("Pass");
        }
        else
        {
            playSound.playError()
            sucIcon.visible = false;
            errIcon.visible = true;
            errIcon.animate()
            busy.visible = false;
            resultCaption.text = qsTr("Fail");
        }

        curResult.text = curResult.text + "\n" + values

        console.log("sequence complete:", success)
    }


    ColumnLayout {
        id: col
        anchors.fill: parent
        spacing: 16
        RowLayout {
            Layout.minimumWidth: col.width
            Layout.maximumWidth: col.width
            spacing: 16
            Pane {
                id: equippedDevice
                Material.elevation: 6
                Layout.minimumWidth: 200
                Layout.minimumHeight: 200
            }

            Pane {
                id: plotResults
                Material.elevation: 6
                Layout.fillWidth: true
                //Layout.minimumWidth: 400
                Layout.minimumHeight: 200
            }

            Pane {
                id: runResults
                Material.elevation: 6
                Layout.minimumWidth: 344
                Layout.maximumWidth: 344
                Layout.minimumHeight: 200
                Layout.maximumHeight: 200
                padding: 0

                ColumnLayout {
                    anchors.fill: parent
                    spacing: 0
                    Layout.margins: 0

                    RowLayout {
                        Layout.leftMargin: 16
                        Layout.rightMargin: 32
                        Layout.topMargin: 24
                        Layout.bottomMargin: 8
                        spacing: 16
                        Layout.minimumWidth: 344-80-32-16
                        Layout.maximumWidth: 344-80-32-16

                        ColumnLayout {

                            Layout.minimumWidth: 344-80-32-16
                            Layout.maximumWidth: 344-80-32-16
                            spacing: 0
                            Layout.margins: 0

                            /*
                            Rectangle {
                                Layout.fillWidth: true
                                Layout.minimumHeight: 16
                                Layout.maximumHeight: 16
                                color: "yellow"
                            }
                            */

                            Text {
                                Layout.fillWidth: true
                                id: resultDevID
                                font.family: "Roboto"
                                font.pixelSize: 10
                                text: "Unbekanntes Gerät"
                                color: "#de000000"
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignTop
                                maximumLineCount: 1
                            }

                            Text {
                                Layout.topMargin: 14
                                Layout.fillWidth: true
                                id: resultCaption
                                font.family: "Roboto"
                                //font.bold: true
                                font.pixelSize: 24
                                text: "INIT"
                                color: "#de000000"
                            }
                            Text {
                                Layout.topMargin: 12
                                Layout.fillWidth: true
                                id: txtStart
                                font.family: "Roboto"
                                font.pixelSize: 14
                                text: "Start: xxx"
                                color: "#99000000"
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignTop
                                maximumLineCount: 1
                            }
                            Text {
                                Layout.fillWidth: true
                                Layout.topMargin: 2
                                id: txtDuration
                                font.family: "Roboto"
                                font.pixelSize: 14
                                text: "Dauer: xxx"
                                color: "#99000000"
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignTop
                                maximumLineCount: 1
                            }
                        } /* ColumnLayout Text */

                        ColumnLayout {
                            Rectangle {
                                /* icon placeholder */
                                id: iconRect
                                Layout.minimumWidth: 80
                                Layout.maximumWidth: 80
                                Layout.minimumHeight: 80
                                Layout.maximumHeight: 80
                                color: "transparent"
                                BusyIndicator {
                                    id: busy
                                    visible: false
                                    anchors.fill: parent
                                    Material.accent: Material.color(root.secondaryColor)
                                }
                                SuccessIcon {
                                    id: sucIcon
                                    finalRadius: 40
                                    replayFactor: 2
                                    anchors.fill: parent
                                    circleColor: Material.color(Material.Green)
                                }
                                ErrorIcon {
                                    id: errIcon
                                    finalRadius: 40
                                    replayFactor: 2
                                    anchors.fill: parent
                                    circleColor: Material.color(Material.Red)
                                }
                            } /* Icon placeholder */
                            Rectangle {
                                Layout.fillHeight: true
                                Layout.fillWidth: true
                                color: "transparent"
                            }
                        } /* Column Layout Icon */

                    }

                    RowLayout {
                        Layout.leftMargin: 8
                        Layout.topMargin: 8
                        spacing:0
                        Button {
                            text: "Zeige Ergebnisse"
                            Material.elevation: 0
                            Material.foreground: Material.color(root.secondaryColor)
                        }
                    }

                } /* Column Layout */

                Component.onCompleted: {

                }
            }
        }
        RowLayout {
            Layout.fillHeight: true
            Layout.minimumWidth: col.width
            Layout.maximumWidth: col.width
            spacing: 16
            Pane {
                id: runResultsTable
                Material.elevation: 6
                Layout.fillHeight: true
                Layout.fillWidth: true


                ScrollView {
                    clip: true
                    anchors.fill: parent
                    TextArea {
                        id: curResult
                        anchors.fill: parent

                        font.family: "Courier New"
                        font.pixelSize: 14
                        color: "#99000000"

                    }
                }

                /*
                TableView {
                    anchors.fill: parent
                    TableViewColumn {
                        role: "title"
                        title: "Title"
                        width: 100
                    }
                    TableViewColumn {
                        role: "author"
                        title: "Author"
                        width: 200
                    }
                    model: libraryModel
                }
                ListModel {
                    id: libraryModel
                    ListElement {
                        title: "A Masterpiece"
                        author: "Gabriel"
                    }
                    ListElement {
                        title: "Brilliance"
                        author: "Jens"
                    }
                    ListElement {
                        title: "Outstanding"
                        author: "Frederik"
                    }
                }
                */


            }
            Pane {
                id: nonProcessParams
                Material.elevation: 6
                Layout.minimumWidth: 200
                Layout.fillHeight: true
            }
        }

        RowLayout {
            Layout.minimumHeight: 50
            Layout.maximumHeight: 50
            Layout.minimumWidth: col.width
            Layout.maximumWidth: col.width
            spacing: 16
            Rectangle {
                id: spacer
                color: "transparent"
                Layout.fillWidth: true
            }
            Button {
                id: manualStart
                text: qsTr("manueller Start")
                Material.accent: Material.color(root.secondaryColor)
                highlighted: true
                onClicked: {
                    var rv = testSuite.run()
                    console.log("trigger success: ", rv);
                }
            }
        }

    } /* ColumnLayout */

    Timer {
        id: busyTxtTimer
        interval: 300; running: true; repeat: true
        onTriggered: {
            internal._curIdx = internal._curIdx+1;
            if (internal._curIdx>3)
                internal._curIdx = 0;

            var txt = "Busy"
            if (testSuite.isRunning() === true)
            {
                busy.visible = true;
                for (var i=0;i<internal._curIdx%4;i++){
                     txt = txt +"."
                }
                resultCaption.text = txt;
            }

        }
    }


}
