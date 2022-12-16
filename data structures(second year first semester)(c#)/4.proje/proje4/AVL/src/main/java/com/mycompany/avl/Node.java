/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.avl;

/**
 *
 * @author emirg
 */
public class Node { // Düğüm class'ı
    int key, height;        // Her bir düğümün değeri ve yüksekliği oluyor.
    Node left, right;       // Her bir düğüm nesnesi sağındaki ve solundaki düğümleri data olarak tutuyor.
 
    Node(int d) {
        key = d;
        height = 1;
    }

}
