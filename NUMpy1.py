{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMx4eOKik/XWid3C+QS0yjy",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kishore8220/Pandas/blob/main/NUMpy1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 81,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5V7zoOPHVvSE",
        "outputId": "74828441-2256-432c-c71e-69b5b119ac23"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5]\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "arr=np.array([1,2,3,4,5])# 1 dimensional array\n",
        "print(arr)\n",
        "print(arr.ndim)# checks the dimension of the ndarray"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr=np.array([[1,2,3],[4,5,6]])# 2 dimensional array\n",
        "print(arr)\n",
        "print(arr.ndim)# checks the dimension of the ndarray"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SIPVFYfBW6kC",
        "outputId": "17781d66-120a-4cf8-e7df-bb0f074f3629"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]]\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "arr = np.array([[[1,3],[1,2],[4,5]]])# 3 dimensional array\n",
        "print(arr)\n",
        "print(arr.ndim)# checks the dimension of the ndarray"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wxr6CKYYXfWs",
        "outputId": "e4c172fb-ac5a-47c5-e7c6-a730a4d88d31"
      },
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[1 3]\n",
            "  [1 2]\n",
            "  [4 5]]]\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "arr = np.array([[10,20,30,40],[50,60,70,80]])\n",
        "print(arr.shape)# show shape of array\n",
        "new=arr.reshape(4,2)# reshape the array\n",
        "print(new)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TB1Eft3yY2Yr",
        "outputId": "fcdc9b7d-2827-4322-8dfd-d51ab4a75e80"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(2, 4)\n",
            "[[10 20]\n",
            " [30 40]\n",
            " [50 60]\n",
            " [70 80]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.array([1,2,4])\n",
        "arr1=np.array([3,4,5])\n",
        "new = np.concatenate((arr,arr1))# add 2 arrays\n",
        "print(new)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8VWHaa3rY2eT",
        "outputId": "87175d71-5281-4ebe-c360-0c3f05916bf6"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 4 3 4 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "a = np.array([\"HELLO\",\"WORLD\"])\n",
        "b=np.array([\"welcome\",\"numpy\"])\n",
        "re=np.char.add(a,b)# add or join 2 arrays\n",
        "print(re)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gGWJn1HWahlT",
        "outputId": "76037971-f106-4bca-f589-afa2f29131a7"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['HELLOwelcome' 'WORLDnumpy']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "str=\"hello world\"\n",
        "b=np.char.upper(str)# upper the string\n",
        "print(b)\n",
        "b=np.char.lower(str)# lower the string\n",
        "print(b)\n",
        "print(str)\n",
        "a=np.char.replace(str,'hello','my')# replace new string or char\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HcPeJRbvcGpX",
        "outputId": "a2c56ed0-3437-426f-fcf5-e7b5484cae95"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HELLO WORLD\n",
            "hello world\n",
            "hello world\n",
            "my world\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "a= np.array([10,20,30])\n",
        "b=np.array([40,50,60])\n",
        "c=np.add(a,b)# ADDITION OF 2 ARRAYS\n",
        "d=np.subtract(a,b)# SUBTRACTION OF 2 ARRAYS\n",
        "print(\"Addition    : \",c)\n",
        "print(\"Subtraction : \",d)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aa6e2H60eafN",
        "outputId": "e5ac8534-0143-4ae2-a0a2-fd43aa7579a5"
      },
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Addition    :  [50 70 90]\n",
            "Subtraction :  [-30 -30 -30]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr=np.array([[4,3,8],[10,2,3],[5,8,24]],dtype='int64')\n",
        "print(arr.ndim)# return no.of dimension\n",
        "print(arr.dtype)# return the datatype of array\n",
        "print(arr.size)# return the size or total elments of array\n",
        "print(arr.shape)# return shape of array(row,column)\n",
        "print(arr.itemsize)# return itemsize\n",
        "print(arr.data)# return memory of array"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y96--jT2fcbO",
        "outputId": "78132b6f-5a6f-47a9-bb78-5b9521c6252c"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "int64\n",
            "9\n",
            "(3, 3)\n",
            "8\n",
            "<memory at 0x7f904deb1630>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr=np.array([[4,3,8],[10,2,3],[5,8,24]],dtype='int64')\n",
        "print(np.amin(arr))# minimum of array\n",
        "print(np.amin(arr,axis=0))# minimum of arrary of row or columns\n",
        "print(np.amax(arr))# maximum of array\n",
        "print(np.max(arr))# maximum of array\n",
        "print(np.amax(arr,axis=1))# maximum of arrary of row or columns\n",
        "print(np.median(arr,axis=0))# return median of array\n",
        "print(np.mean(arr))# return mean of array\n",
        "print(np.std(arr))# return standard divison of array\n",
        "print(np.var(arr))# return variance of array\n",
        "print(np.percentile(arr,40))# return percentile of array"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z91Ynsg7g5WU",
        "outputId": "6e1abd1c-b54c-419c-bad5-08be33f85d74"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "[4 2 3]\n",
            "24\n",
            "24\n",
            "[ 8 10 24]\n",
            "[5. 3. 8.]\n",
            "7.444444444444445\n",
            "6.396372428721891\n",
            "40.91358024691359\n",
            "4.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.array([1,2,3,4,5,6,7,8,9,10])\n",
        "np.where(arr%2==0,\"Even\",\"Odd\")# where function\n",
        "co=[arr<5,arr>5]# conditions\n",
        "cho=[arr**2,arr+5]# choice list\n",
        "np.select(co,cho,default=arr)# select function\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lbPXtsTei-ae",
        "outputId": "e1b1d84d-32d9-4890-b44c-811401e7da0c"
      },
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 1,  4,  9, 16,  5, 11, 12, 13, 14, 15])"
            ]
          },
          "metadata": {},
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.array([1,2,3,4,5])\n",
        "print(arr[1])\n",
        "arr1= np.array([[1,2,3,4],[5,6,7,8]])\n",
        "print(arr1)\n",
        "print(arr1[0,2])\n",
        "arr1= np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])\n",
        "print(arr1)\n",
        "print(arr1[0,2,3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ujR06qwWsMXD",
        "outputId": "1d48cc8b-d6dc-46dd-e77b-5939074e1f67"
      },
      "execution_count": 117,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "[[1 2 3 4]\n",
            " [5 6 7 8]]\n",
            "3\n",
            "[[[ 1  2  3  4]\n",
            "  [ 5  6  7  8]\n",
            "  [ 9 10 11 12]]]\n",
            "12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BzAtXPVft3Tt"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}