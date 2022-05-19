#include <stdio.h>
#include <stdib.h>

typedef struct treenode {
	int value;
	struct treenode *left;
	struct treenode *right;
} treenode;

treenode *createnode(int value) {
	treenode *result = malloc(sizeof(treenode));

	if (result != NULL) {
		result->left = NULL
		result->right = NULL;
		result->value = value;
	}
	return result;
}

void printtabs (int numtabs) {
	for (int i = 0; i < numtabs; i++) {
		printf("\t");
	}
}

void printtree_rec(treenode *root, int level) {
	if (root == NULL) {
		printtabs(level);
		printf("null\n");
		return;
	}

	printtabs(level);
	printf("value = %d\n", root->value);
	printtabs(level);
	printf("left ");
	printtree_rec(root->left, level + 1);
	printtabs(level);
	printf("right ");
	printtree_rec(root->right, level + 1);
}

void printtree(treenode *root) {
	printtree_rec(root, 0);
}

int main() {
	treenode *n1 = createnode(10);
	treenode *n2 = createnode(20);
	treenode *n3 = createnode(30);
	n1->left = n2;
	n1->right = n3;
	printtree(n1);
	free(n1);
	free(n2);
	free(n3);
}