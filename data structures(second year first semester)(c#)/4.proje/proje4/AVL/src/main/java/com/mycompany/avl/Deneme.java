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
public class Deneme {
    public static void main(String[] args) {
        AVL tree = new AVL();   // Ağacı yaratıyoruz.
 
        
        tree.root = tree.insert(tree.root, 5);      // Ağaca insert methodu yardımıyla elemanlar ekliyoruz.
        tree.root = tree.insert(tree.root, 25);
        tree.root = tree.insert(tree.root, 35);
        tree.root = tree.insert(tree.root, 45);
        tree.root = tree.insert(tree.root, 55);
        tree.root = tree.insert(tree.root, 30);     // Ağacı yazdırıyoruz.
        
        tree.preOrder(tree.root);
}
}
