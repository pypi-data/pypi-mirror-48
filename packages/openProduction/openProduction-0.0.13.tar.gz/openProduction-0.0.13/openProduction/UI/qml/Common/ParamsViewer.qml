import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.0

Item {
    id: root
    property QtObject model: null

    onModelChanged: {
        if (model !== null) {
            model.setParent(content)
            console.log(model.getKeys());

            var component = Qt.createComponent('Rectangle {height:50, width:50, color:"green"}');
            var sprite = component.createObject(content, {"x": 0, "y": 0});
        }
    }

    Rectangle {
        id: content
        anchors.fill: parent
        color: "red"
/*
        TableView {
            id: tableView
            objectName: "tableView"
            horizontalScrollBarPolicy: -1
            selectionMode: SelectionMode.SingleSelection
            anchors.fill: parent

            TableViewColumn {
                id: titleColumn
                title: "Beschreibung"
                role: "key"
                movable: false
                resizable: false
                width: tableView.viewport.width - authorColumn.width
            }

            TableViewColumn {
                id: authorColumn
                title: "Wert"
                role: "value"
                movable: false
                resizable: false
                width: tableView.viewport.width / 3
            }
            model: ListModel {
                id: libraryModel
                ListElement {
                    key: "Test 123"
                    value: "10"
                }
                ListElement {
                    key: "Test Text"
                    value: "Hello world"
                }
                ListElement {
                    key: "Test bool"
                    value: "true"
                }
            }

            itemDelegate: Rectangle {
                Text {
                    anchors {
                        verticalCenter: parent.verticalCenter
                        left: parent.left
                    }
                    color: "black"
                    text: styleData.value
                }

                MouseArea {
                    id: cellMouseArea
                    anchors.fill: parent
                    onClicked: {
                        // Column index are zero based
                        if (styleData.column === 1) {
                            loader.visible = true
                            loader.item.forceActiveFocus()
                        }
                    }
                }

                Loader {
                    id: loader
                    anchors {
                        verticalCenter: parent.verticalCenter
                        left: parent.left
                    }
                    height: parent.height
                    width: parent.width
                    visible: false
                    sourceComponent: visible ? input : undefined

                    Component {
                        id: input
                        TextField {
                            anchors {
                                fill: parent
                            }
                            text: ""
                            onAccepted: {
                                // DO STUFF
                                loader.visible = false
                            }

                            onActiveFocusChanged: {
                                if (!activeFocus) {
                                    loader.visible = false
                                }
                            }
                        }
                    }
                }
            }
        }
        */
    }
}
