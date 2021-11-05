#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* head = malloc(sizeof(struct ListNode));
    int carry = 0;
    head->next = NULL;
    struct ListNode* list = head;
    list->val = (l1->val+l2->val+carry)%10;
    if(l1->val+l2->val+carry > 9){
        carry = 1;
    }else{
        carry = 0;
    }
    l1 = l1->next;
    l2 = l2->next;
    while(l1 || l2){
        struct ListNode* tpm = malloc(sizeof(struct ListNode));
        list->next = tpm;
        tpm->next=NULL;
        int val1 = l1 && l1->val ? l1->val : 0;
        int val2 = l2 && l2->val ? l2->val : 0;
        tpm->val = (val1+val2+carry)%10;
        if(val1+val2+carry > 9){
            carry = 1;
        }else{
            carry = 0;
        }
        l1 = l1 ? l1->next : l1;
        l2 = l2 ? l2->next : l2;
        list = list->next;
    }
    if(carry){
        struct ListNode* tpm = malloc(sizeof(struct ListNode));
        list->next = tpm;
        tpm->next=NULL;
        tpm->val=carry;
    }
    return head;
}