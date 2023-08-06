import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.0

Item {
    id: root
    property QtObject model: null

    Rectangle {
        id: content
        anchors.fill: parent
        color: "white"

        ListView {
            anchors.fill: parent
            model: root.model
            delegate: Item {
                function getSourceComponent(key, value, type) {
                    if (type === "BOOL")
                    {
                        renderType.sourceComponent = boolParam
                        renderType.item.text = key
                        renderType.item.checked = value
                    }
                }


                Component.onCompleted: {
                    getSourceComponent(key, value, type);
                }

                width: 180; height: 40
                Loader {
                    id: renderType
                }

            }
        }

        Component {
            id: boolParam
            //property alias text: checkBox.text
            //property alias checked: checkBox.checked
            CheckBox {
                id: checkBox
                onCheckedChanged: {
                    if (root.model !== null)
                        root.model.keyChangedFromUI(text, checked, "BOOL");
                }
            }
        }

    }
}
